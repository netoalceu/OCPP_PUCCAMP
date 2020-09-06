from datetime import datetime

from ocpp.routing import on, after
from ocpp.v20 import call_result, ChargePoint as cp
#from ocpp.v16.enums import *  # comferir estes enuns, devido as diferenças de JSON Schema
from src.timerRegistration import now
from src.enumsV20 import *

valid_tokens = ["a36ef7b0", "1234", "12345", "1111", "2222", 987]

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

    ################## AUTHORIZE ##########################
    @on(Action.Authorize)
    def on_authorize(self, id_token):
        if id_token in valid_tokens:
            return call_result.AuthorizePayload(
                id_token_info={
                    "status": AuthorizationStatus.accepted},
                certificate_status='',
                evse_id=[]
            )
        else:
            return call_result.AuthorizePayload(
                id_token_info={
                    "status": AuthorizationStatus.invalid},
                certificate_status='',
                evse_id=[]
            )

    @after(Action.Authorize)
    def after_authorize(self, id_token):
        print("Authorization requested from: ", id_token)
