from ocpp.v16.enums import *  # comferir estes enuns, devido as diferenças de JSON Schema


class AuthorizationStatus(AuthorizationStatus):
    nocredit = 'NoCredit'
    notallowedtypeevse = 'NotAllowedTypeEVSE'
    notAtthislocation = 'NotAtThisLocation'
    notatthistime = 'NotAtThisTime'
    unknown = 'Unknown'
