from ocpp.routing import on, after
from ocpp.v20 import call, call_result, ChargePoint as cp
from src.tools import now
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
    ############## CHANGE AVAILABILITY #######################
    @on(Action.ChangeAvailability)
    def on_change_availability(self, evse_id, operational_status):
        return call_result.ChangeAvailabilityPayload(
            status=AvailabilityStatus.accepted
        )

    @after(Action.ChangeAvailability)
    def after_change_availability(self, evse_id, operational_status):
        print("Change avilability ready")
    """
    ################# REMOTE START TRANSACTION ##################
    async def send_remote_start_transaction(self, id_tag_cs):

        request = call.RemoteStartTransactionPayload(
            id_tag=id_tag_cs
        )

        response = await self.call(request)

        if response.status == RemoteStartStopStatus.accepted:
            print("Start remote transaction accepted from charge point!")
        else:
            print("Start remote transaction rejected from charge point!")

    ################# REMOTE END TRANSACTION ##################
    async def send_remote_end_transaction(self, transaction_id_cs):

        request = call.RemoteStopTransactionPayload(
            transaction_id=transaction_id_cs
        )

        response = await self.call(request)

        if response.status == RemoteStartStopStatus.accepted:
            print("Stop remote transaction accepted from charge point!")
        else:
            print("Stop remote transaction rejected from charge point!")
    """

