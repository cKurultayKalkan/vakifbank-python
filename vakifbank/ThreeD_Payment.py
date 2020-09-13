import os
import pathlib

from vakifbank.routes import ServiceUrl
from vakifbank.consts import *
from vakifbank.service import HttpClient
from vakifbank.auth import Auth
from xml.etree.ElementTree import Element, SubElement, tostring
from urllib.parse import urlencode
import xmltodict


class ThreeDPayment:
    order_id = ""
    amount = ""
    pan = ""
    expiry = ""
    currency = ""
    success_url = ""
    fail_url = ""
    card_type = ""
    pareq = ""
    acs_url = ""
    term_url = ""
    md = ""
    brand = ""
    start_response = ""
    enrollment_response = ""

    def __init__(self, credentials):
        self.url = ServiceUrl('VPos', DEBUG)
        self.http = HttpClient
        self.auth = Auth.getInstance(credentials).getDict()

    def prepare(self, order_id, amount, pan, expiry, success_url="http://localhost:8000/success", fail_url="http://localhost:8000/success", currency="949", card_type="100"):
        self.order_id = order_id
        self.amount = amount
        self.pan = pan
        self.expiry = expiry
        self.currency = currency
        self.success_url = success_url
        self.fail_url = fail_url
        self.card_type = card_type

    def start(self):
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
        self.start_response = response
        print(response.encode('utf8'))
        return response

    def enrollment_result(self):
        result = xmltodict.parse(self.start_response)
        root = dict(result).get('IPaySecure')
        error_code = root.get('MessageErrorCode')
        message = dict(root.get("Message"))
        order_id = root.get("VerifyEnrollmentRequestId")
        res = dict(message.get("VERes"))
        self.pareq = res.get("PaReq")
        self.acs_url = res.get("ACSUrl")
        self.term_url = res.get("TermUrl")
        self.md = res.get("MD")
        self.brand = res.get("ACTUALBRAND")
        status = res.get("Status")
        self.enrollment_response = res
        if status != 'Y':
            return {'status': False, 'message': error_code}
        return {'status': True}

    def get_acs_html(self):
        res = self.enrollment_response
        template_path = pathlib.Path(__file__).parent.absolute()
        html_template = open(os.path.join(template_path, 'html', 'pareq_to_acs.html'), 'r', encoding="utf-8")
        t = html_template.read()
        for m in res:
            t = t.replace('{{' + m + '}}', res[m])
        return t
