from .routes import ServiceUrl
from .consts import *
from .service import HttpClient
from .auth import Auth
from xml.etree.ElementTree import Element, SubElement, tostring
from urllib.parse import urlencode


class ThreeDPayment:
    MerchantId = ""
    MerchantPassword = ""
    VerifyEnrollmentRequestId = ""
    Pan = ""
    ExpiryDate = ""
    PurchaseAmount = ""  # 5.4
    Currency = "840"
    BrandName = ""
    SuccessUrl = ""
    FailureUrl = ""
    InstallmentCount = ""
    IsRecurring = ""
    RecurringFrequency = ""
    RecurringEndDate = ""
    MerchantType = ""
    SubMerchantId = ""

    def __init__(self):
        self.url = ServiceUrl('VPos', DEBUG)
        self.http = HttpClient
        self.auth = Auth.getInstance().getDict()

    def start(self, req):
        data = {
            "VerifyEnrollmentRequestId": req.order_id,
            "PurchaseAmount": req.amount,
            "Pan": req.pan,
            "ExpiryDate": req.expiry,
            "Currency": req.currency,
            "SuccessUrl": req.success_url,
            "FailureUrl": req.fail_url
            # "BrandName"
        }

        data.update(self.auth)
        payload = urlencode(data)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        response = self.http.post(self.url, payload, headers)
        print(response.encode('utf8'))
