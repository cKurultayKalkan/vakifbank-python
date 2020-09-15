from vakifbank.Routes import ServiceUrl
from vakifbank.config.consts import *
from vakifbank.Service import HttpClient
from vakifbank.Auth import Auth

import xmltodict


class VPos:
    def __init__(self, credentials=None, debug=None, three_d=None):
        debug_ = debug if debug is not None else DEBUG
        self.url = ServiceUrl('VPos', debug_)
        self.http = HttpClient
        if credentials is None and three_d:
            self.auth = three_d.auth.getDict()
        elif credentials:
            self.auth = Auth.getInstance(credentials).getDict()
        else:
            raise Exception("You need to supply credentials")

    def request_provision(self, req):
        card = {
            'Pan': req.get("Pan"),
            'Cvv': req.get("Cvv"),
            'Expiry': req.get('Expiry')
        }

        confirm = {
            'ECI': req.get("ECI"),
            'CAVV': req.get("CAVV"),
            'MpiTransactionId': req.get("VerifyEnrollmentRequestId"),
        }
        data = {
            'TransactionType': 'Sale',
            'CurrencyAmount': req.get("CurrencyAmount"),
            'CurrencyCode': req.get("PurchCurrency"),
            'ClientIp': req.get('IP'),
            'TransactionDeviceSource': '0',
            'MerchantId': self.auth.get('MerchantId'),
            'Password': self.auth.get('MerchantPassword'),
            'TerminalNo': self.auth.get('HostTerminalId')
        }

        data.update(confirm)
        data.update(card)
        data = {
            'VposRequest': data
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        xmldata = xmltodict.unparse(data).replace(' ', '').replace('<?xmlversion="1.0"encoding="utf-8"?>', '')
        send_data = 'prmstr=' + xmldata
        res = self.http.post(self.url.provision, send_data, headers)
        return res
