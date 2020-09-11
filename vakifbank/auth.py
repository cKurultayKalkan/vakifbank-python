from .consts import *


class Auth:
    __instance = None

    @staticmethod
    def getInstance():
        if Auth.__instance is None:
            Auth(HostMerchantId, HostTerminalId, HostPassword)
        return Auth.__instance

    def __init__(self, merchant_id, terminal_no, password):
        self.HostMerchantId = merchant_id
        self.HostTerminalId = terminal_no
        self.MerchantPassword = password
        if Auth.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Auth.__instance = self

    def getDict(self):
        return {
            "MerchantId": self.HostMerchantId,
            "MerchantPassword": self.MerchantPassword,
            "HostTerminalId": self.HostTerminalId,
        }
