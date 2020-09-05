from datetime import datetime

from ocpp.routing import on, after
from ocpp.v20 import ChargePoint as cp
from ocpp.v20 import call_result
from ocpp.v16.enums import *

class ChargePointOperator(cp):
    ################## BOOT NOTIFICATION #################
    @on('BootNotification')
    def on_boot_notification(self, charging_station, reason, **kwargs):
        print(datetime.utcnow().isoformat(), 'Got a BootNotification!')
        return call_result.BootNotificationPayload(
            current_time=datetime.utcnow().isoformat(),
            interval=10,
            status='Accepted'
        )

    @after('BootNotification')
    def after_boot_notification(self, charging_station, reason, **kwargs):
        print("Boot Notification from:")
        print("ChargePoint Vendor: ", charging_station)
        print("ChargePoint Model: ", reason)

    ################## HEARTBEAT ##########################
    @on('Heartbeat')
    def on_heartbeat(self):
        print(datetime.utcnow().isoformat(), 'On a Heartbeat!')
        return call_result.HeartbeatPayload(
            current_time=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z"
        )

    @after('Heartbeat')
    def after_heartbeat(self):
        print(datetime.utcnow().isoformat(), 'After - Heartbeat')
