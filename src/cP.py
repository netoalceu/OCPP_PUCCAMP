class CP:
  def __init__(self, rfid, connector_id, authorize,
             transaction_id, transaction_status, meter_values):
    self.rfid = rfid
    self.connector_id = connector_id
    self.authorize = authorize
    self.transaction_id = transaction_id
    self.transaction_status = transaction_status
    self.meter_values = meter_values
