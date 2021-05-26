from kuveytturk_pos.Routes import ServiceUrl
from kuveytturk_pos.config.consts import *
from kuveytturk_pos.Service import HttpClient
from kuveytturk_pos.Auth import Auth

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
            'CardNumber': req.get("Pan"),
            'CardExpireDateYear': req.get("Cvv"),
            'CardExpireDateMonth': req.get('Expiry'),
            'CardHolderName': req.get('Expiry'),
            'cardCVV2': req.get('Expiry'),
            'CardType': req.get('Expiry'),
        }

        redirection = {
            'OkUrl': 'https://udef.org.tr/',
            'FailUrl': 'https://udef.org.tr/',
            'HashData': ""
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

        data.update(redirection)
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
