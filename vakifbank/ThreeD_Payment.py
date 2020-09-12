from vakifbank.routes import ServiceUrl
from vakifbank.consts import *
from vakifbank.service import HttpClient
from vakifbank.auth import Auth
from xml.etree.ElementTree import Element, SubElement, tostring
from urllib.parse import urlencode


class ThreeDPayment:
    order_id = ""
    amount = ""
    pan = ""
    expiry = ""
    currency = ""
    success_url = ""
    fail_url = ""
    card_type = ""

    def __init__(self):
        self.url = ServiceUrl('VPos', DEBUG)
        self.http = HttpClient
        self.auth = Auth.getInstance().getDict()

    def prepare(self, order_id, amount, pan, expiry, success_url="http://localhost:8000/success", fail_url="http://localhost:8000/success", currency="949", card_type="100"):
        self.order_id = order_id
        self.amount = amount
        self.pan = pan
        self.expiry = expiry
        self.currency = currency
        self.success_url = success_url
        self.fail_url = fail_url
        self.card_type = card_type

    def start(self, req):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = {
            "VerifyEnrollmentRequestId": self.order_id,
            "PurchaseAmount": self.amount,
            "Pan": self.pan,
            "ExpiryDate": self.expiry,
            "Currency": self.currency,
            "SuccessUrl": self.success_url,
            "FailureUrl": self.fail_url,
            "BrandName": self.card_type
        }
        data.update(self.auth)
        payload = urlencode(data)
        response = self.http.post(self.url.enroll, payload, headers)
        print(response.encode('utf8'))
        return response
