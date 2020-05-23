import asyncio
import websockets
from aiohttp import web
from functools import partial
from datetime import datetime

from ocpp.routing import on
from ocpp.v16 import ChargePoint as cp
from ocpp.v16.enums import Action, RegistrationStatus
from ocpp.v16 import call_result, call


class ChargePoint(cp):
    @on(Action.BootNotification)
    def on_boot_notitication(self, charge_point_vendor, charge_point_model, **kwargs):
        return call_result.BootNotificationPayload(
            current_time=datetime.utcnow().isoformat(),
            interval=10,
            status=RegistrationStatus.accepted,
        )

    async def change_configuration(self, key: str, value: str):
        return await self.call(call.ChangeConfigurationPayload(key=key, value=value))


class CentralSystem:
    def __init__(self):
        self._chargers = {}

    def register_charger(self, cp: ChargePoint) -> asyncio.Queue:
        """ Register a new ChargePoint at the CSMS. The function returns a
        queue.  The CSMS will put a message on the queue if the CSMS wants to
        close the connection.
        """
        queue = asyncio.Queue(maxsize=1)

        # Store a reference to the task so we can cancel it later if needed.
        task = asyncio.create_task(self.start_charger(cp, queue))
        self._chargers[cp] = task

        return queue

    async def start_charger(self, cp, queue):
        """ Start listening for message of charger. """
        try:
            await cp.start()
        except Exception as e:
            print(f"Charger {cp.id} disconnected: {e}")
        finally:
            # Make sure to remove referenc to charger after it disconnected.
            del self._chargers[cp]

            # This will unblock the `on_connect()` handler and the connection
            # will be destroyed.
            await queue.put(True)

    async def change_configuration(self, key: str, value: str):
        for cp in self._chargers:
            await cp.change_configuration(key, value)

    def disconnect_charger(self, id: str):
        for cp, task in self._chargers.items():
            if cp.id == id:
                task.cancel()
                return

        raise ValueError(f"Charger {id} not connected.")


async def change_config(request):
    """ HTTP handler for changing configuration of all charge points. """
    data = await request.json()
    csms = request.app["csms"]

    await csms.change_configuration(data["key"], data["value"])

    return web.Response()


async def disconnect_charger(request):
    """ HTTP handler for disconnecting a charger. """
    data = await request.json()
    csms = request.app["csms"]

    try:
        csms.disconnect_charger(data["id"])
    except ValueError as e:
        print(f"Failed to disconnect charger: {e}")
        return web.Response(status=404)

    return web.Response()


async def on_connect(websocket, path, csms):
    """ For every new charge point that connects, create a ChargePoint instance
    and start listening for messages.

    The ChargePoint is registered at the CSMS.

    """
    charge_point_id = path.strip("/")
    cp = ChargePoint(charge_point_id, websocket)

    print(f"Charger {cp.id} connected.")

    # If this handler returns the connection will be destroyed. Therefore we need some
    # synchronization mechanism that blocks until CSMS wants to close the connection.
    # An `asyncio.Queue` is used for that.
    queue = csms.register_charger(cp)
    await queue.get()


async def create_websocket_server(csms: CentralSystem):
    handler = partial(on_connect, csms=csms)
    return await websockets.serve(handler, "0.0.0.0", 9000, subprotocols=["ocpp1.6"])


async def create_http_server(csms: CentralSystem):
    app = web.Application()
    app.add_routes([web.post("/", change_config)])
    app.add_routes([web.post("/disconnect", disconnect_charger)])

    # Put CSMS in app so it can be accessed from request handlers.
    # https://docs.aiohttp.org/en/stable/faq.html#where-do-i-put-my-database-connection-so-handlers-can-access-it
    app["csms"] = csms

    # https://docs.aiohttp.org/en/stable/web_advanced.html#application-runners
    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, "localhost", 8080)
    return site


async def main():
    csms = CentralSystem()

    websocket_server = await create_websocket_server(csms)
    http_server = await create_http_server(csms)

    await asyncio.wait([websocket_server.wait_closed(), http_server.start()])


if __name__ == "__main__":
    asyncio.run(main())