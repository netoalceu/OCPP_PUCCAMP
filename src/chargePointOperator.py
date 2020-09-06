from datetime import datetime

from ocpp.routing import on, after
from ocpp.v20 import call_result, ChargePoint as cp
from ocpp.v16.enums import *  # comferir estes enuns, devido as diferenças de JSON Schema
from src.timerRegistration import now


class ChargePointOperator(cp):

    ################## BOOT NOTIFICATION #################
    @on(Action.BootNotification)
    def on_boot_notification(self, charging_station, reason, **kwargs):
        print(now() + ' Got a BootNotification!')
        return call_result.BootNotificationPayload(
            current_time=now(),
            interval=10,
            status=RegistrationStatus.accepted
        )

    @after(Action.BootNotification)
    def after_boot_notification(self, charging_station, reason, **kwargs):
        print("Boot Notification from:")
        print("ChargePoint Vendor: ", charging_station)
        print("ChargePoint Model: ", reason)

    ################## HEARTBEAT ##########################
    @on(Action.Heartbeat)
    def on_heartbeat(self):
        print(now(), ' On a Heartbeat!')
        return call_result.HeartbeatPayload(
            current_time=now()
        )

    @after(Action.Heartbeat)
    def after_heartbeat(self):
        print(now(), ' After - Heartbeat')
