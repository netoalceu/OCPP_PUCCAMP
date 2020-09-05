#!/usr/bin/env python

import asyncio
import websockets


async def echo(websocket, path):
    async for message in websocket:
        print("recebi ", message)
        await websocket.send('resposta do servidor: '+ message)


asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()
