from ocpp.routing import on, after
from ocpp.v20 import call_result, ChargePoint as cp
from src.tools import now, HEARTBEAT_INTERVAL
from src.enumsV20 import *

valid_tokens = ["a36ef7b0", "1234", "12345", "1111", "2222", 987]


class ChargePointOperator(cp):

    ################## BOOT NOTIFICATION #################
    @on(Action.BootNotification)
    def on_boot_notification(self, charging_station, reason, **kwargs):
        print(now() + ' Got a BootNotification!')
        return call_result.BootNotificationPayload(
            current_time=now(),
            interval=HEARTBEAT_INTERVAL,
            status=RegistrationStatus.accepted
        )

    @after(Action.BootNotification)
    def after_boot_notification(self, charging_station, reason, **kwargs):
        print(now(), " Boot Notification from: ", charging_station, ", cause ", reason)

    ################## HEARTBEAT ##########################

    @on(Action.Heartbeat)
    def on_heartbeat(self):
        print(now(), ' On a Heartbeat!')
        return call_result.HeartbeatPayload(
            current_time=now()
        )

    """
    @after(Action.Heartbeat)
    def after_heartbeat(self):
        print(now(), ' After - Heartbeat')
    """

    ################## AUTHORIZE ##########################
    @on(Action.Authorize)
    def on_authorize(self, id_token):
        if id_token['id_token'] in valid_tokens:
            print(now(), 'Token Accepted')
            return call_result.AuthorizePayload(
                id_token_info={
                    "status": AuthorizationStatus.accepted}
            )
        else:
            print(now(), 'Token Invalid')
            return call_result.AuthorizePayload(
                id_token_info={
                    "status": AuthorizationStatus.invalid}
            )

    """
    @after(Action.Authorize)
    def after_authorize(self, id_token):
        print("Authorization requested from: ", id_token)
    """

    ################## START TRANSACTION ####################
    @on(Action.RequestStartTransaction)
    def on_request_start_transaction(self, remote_start_id, id_token):
        if id_token['id_token'] == '123':
            print(now(), 'Starting Transaction')
            return call_result.RequestStartTransactionPayload(
                status=AvailabilityStatus.accepted
            )
        else:
            print(now(), 'Wrong ID_Token. Transaction did not initiate')
            return call_result.RequestStartTransactionPayload(
                status=AvailabilityStatus.rejected
            )
    """
    @after(Action.RequestStartTransaction)
    def after_start_transaction(self, connector_id, id_tag, meter_start, timestamp):
        print("Started transaction in connector {}, from {}, starting meter: {}, timestamp {}".format(connector_id,
    """

    ################## METER VALUES ##########################
    @on(Action.MeterValues)
    def on_meter_values(self, evse_id, meter_value):
        print(now(), evse_id, meter_value)
        return call_result.MeterValuesPayload(
        )
    """
    @after(Action.MeterValues)
    def after_meter_values(self, evse_id, meter_value):
        print("Received meter values")
    """

    ################## STOP TRANSACTION ##########################
    @on(Action.RequestStopTransaction)
    def on_request_stop_transaction(self, transaction_id):
        print(now(), 'Finished Transaction', transaction_id)
        return call_result.RequestStopTransactionPayload(
            status=AvailabilityStatus.accepted
        )
    """
    @after(Action.RequestStopTransaction)
    def after_request_stop_transaction(self, meter_stop, timestamp, transaction_id):
        print("Stop transaction ", transaction_id, "meter value: ", meter_stop)
    """
