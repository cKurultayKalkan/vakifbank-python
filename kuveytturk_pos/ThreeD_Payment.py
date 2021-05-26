import os
import pathlib

from kuveytturk_pos.Routes import ServiceUrl
from kuveytturk_pos.config.consts import *
from kuveytturk_pos.Service import HttpClient
from kuveytturk_pos.Auth import Auth
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

    def __init__(self, credentials, debug=None):
        debug_ = debug if debug is not None else DEBUG
        self.url = ServiceUrl("VPos", debug_)
        self.http = HttpClient
        self.auth = Auth.getInstance(credentials).getDict()

    def prepare(self, order_id, amount, card_holder, pan, expiry_year, expiry_month, card_cvv, success_url, fail_url, currency="949", card_type="100"):
        self.order_id = order_id
        self.card_holder = card_holder
        self.expiry_year = expiry_year
        self.expiry_month = expiry_month
        self.card_cvv = card_cvv
        self.amount = amount
        self.pan = pan
        self.currency = currency
        self.success_url = success_url
        self.fail_url = fail_url
        self.card_type = card_type

    def start(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        card = {
            "CardNumber": self.pan,
            "CardExpireDateYear": self.expiry_year,
            "CardExpireDateMonth": self.expiry_month,
            "CardHolderName": self.card_holder,
            "cardCVV2": self.card_cvv,
            "CardType": self.card_type,
        }
        data = {
            "MerchantOrderId": self.order_id,
            "TransactionSecurity": 3,
            "OkUrl": self.success_url,
            "FailUrl": self.fail_url,
            "HashData": "",
            "CurrencyCode": "0" + self.currency,
            "Amount": self.amount,
            "DisplayAmount": self.amount,
            "InstallmentCount": 0
        }
        data.update(self.auth)
        data.update(card)
        data = {
            'KuveytTurkVPosMessage': data
        }
        payload = urlencode(data)
        response = self.http.post(self.url.enroll, payload, headers)
        self.start_response = response
        return response

    def enrollment_result(self):
        result = xmltodict.parse(self.start_response)
        root = dict(result).get("IPaySecure")
        error_code = root.get("MessageErrorCode")
        error_message = root.get("ErrorMessage")
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
        if status != "Y":
            return {"status": False, "message": error_message, "error_code": error_code}
        return {"status": True}

    def get_acs_html(self):
        template_path = pathlib.Path(__file__).parent.absolute()
        html_template = open(os.path.join(template_path, "html", "pareq_to_acs.html"), "r", encoding="utf-8")
        t = html_template.read()
        for m in self.enrollment_response:
            t = t.replace("{{" + m + "}}", self.enrollment_response[m])
        return t
