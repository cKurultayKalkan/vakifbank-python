from vakifbank.Routes import ServiceUrl
from vakifbank.config.consts import *
from vakifbank.Service import HttpClient
from vakifbank.Auth import Auth
from xml.etree.ElementTree import Element, SubElement, tostring

import xmltodict


class VPos:
    def __init__(self, credentials=None, debug=None, three_d=None):
        debug_ = debug if debug is not None else DEBUG
        self.url = ServiceUrl('VPos', debug_)
        self.http = HttpClient
        if credentials is None and three_d:
            self.auth = three_d.auth
        elif credentials:
            self.auth = Auth.getInstance(credentials).getDict()
        else:
            raise Exception("You need to supply credentials")

    def request_provision(self, req):
        card = {
            'Pan': req.get("Pan"),
            'Cvv': req.get("Cvv"),  # CVV kodu
            'Expiry': req.get('Expiry')  # YYYYMM
        }

        confirm = {
            'ECI': req.get("ECI"),
            'CAVV': req.get("CAVV"),
            'MpiTransactionId': req.get("VerifyEnrollmentRequestId"),
        }
        data = {
            'TransactionType': 'Sale',
            'CurrencyAmount': req.get("PurchAmount"),
            'CurrencyCode': req.get("PurchCurrency"),
            'ClientIp': req.get('IP'),
            'TransactionDeviceSource': '0'
        }

        data.update(confirm)
        data.update(card)
        data.update(self.auth)
        data = {
            'VPosRequest': data
        }

        headers = {
            'Content-Type': 'application/xml',
        }

        xmldata = xmltodict.unparse(data)
        res = self.http.post(self.url.provision, xmldata, headers)
        return res
