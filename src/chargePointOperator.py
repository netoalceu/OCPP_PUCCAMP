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

    """
    ################## START TRANSACTION ##########################
    @on(Action.StartTransaction)
    def on_start_transaction(self, connector_id, id_tag, meter_start, timestamp):
        trans_id = 987
        return call_result.StartTransactionPayload(
            transaction_id=trans_id,
            id_tag_info={
                "status": AuthorizationStatus.accepted
            }
        )

    @after(Action.StartTransaction)
    def after_start_transaction(self, connector_id, id_tag, meter_start, timestamp):
        print("Started transaction in connector {}, from {}, starting meter: {}, timestamp {}".format(connector_id,
                                                                                                      id_tag,
                                                                                                      meter_start,
                                                                                                      timestamp))
    """
    ################## METER VALUES ##########################
    @on(Action.MeterValues)
    def on_meter_values(self, evse_id, meter_value):
        return call_result.MeterValuesPayload(
        )

    @after(Action.MeterValues)
    def after_meter_values(self, evse_id, meter_value):
        print("Received meter values")

    """
    ################## STOP TRANSACTION ##########################
    @on(Action.StopTransaction)
    def on_stop_transaction(self, meter_stop, timestamp, transaction_id):
        return call_result.StopTransactionPayload(
            # id_tag_info={
            #     "status" : AuthorizationStatus.accepted
            # }
        )

    @after(Action.StopTransaction)
    def after_stop_transaction(self, meter_stop, timestamp, transaction_id):
        print("Stop transaction ", transaction_id, "meter value: ", meter_stop)
    """
