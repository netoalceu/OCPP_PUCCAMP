from ocpp.v16.enums import *  # comferir estes enuns, devido as diferenças de JSON Schema

class Action(Action):
    RequestStartTransaction = "RequestStartTransaction"
    RequestStopTransaction = "RequestStopTransaction"


class AuthorizationStatus(AuthorizationStatus):
    nocredit = 'NoCredit'
    notallowedtypeevse = 'NotAllowedTypeEVSE'
    notAtthislocation = 'NotAtThisLocation'
    notatthistime = 'NotAtThisTime'
    unknown = 'Unknown'


class BootReason:
    """
    Result of BootNotification Reason
    """
    ApplicationReset = 'ApplicationReset'
    FirmwareUpdate = 'FirmwareUpdate'
    LocalReset = 'LocalReset'
    PowerUp = 'PowerUp'
    RemoteReset = 'RemoteReset'
    ScheduledReset = 'ScheduledReset'
    Triggered = 'Triggered'
    Unknown = 'Unknown'
    Watchdog = 'Watchdog'


class IdTokenEnumType:
    Central = 'Central'
    eMAID = 'eMAID'
    ISO14443 = 'ISO14443'
    KeyCode = 'KeyCode'
    Local = 'Local'
    NoAuthorization = 'NoAuthorization'
    ISO15693 = 'ISO15693'
