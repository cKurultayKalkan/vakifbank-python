import os
import unittest
import random
from kuveytturk_pos.ThreeD_Payment import ThreeDPayment
from kuveytturk_pos.Vpos import VPos
from tests.test_cards import TEST_CARD
from kuveytturk_pos.config.consts import CURRENCY_TYPES
import xmltodict


class TestThreeD(unittest.TestCase):
    def setUp(self):
        year = TEST_CARD.get('expire_year')
        month = TEST_CARD.get('expire_month')
        expirydate = year[2:] + month
        currency = CURRENCY_TYPES.get(TEST_CARD.get("currency"))
        credentials = {
            "MerchantId": "",
            "CustomerId": "",
            "UserName": "",
            "Password": "",
        }
        self.three_d = ThreeDPayment(credentials)
        self.vpos = VPos(three_d=self.three_d)
        self.data = {
            'card_holder': card_holder,
            'expiry_year': expiry_year,
            'expiry_month': expiry_month,
            'card_cvv': card_cvv,
            'currency': currency,
            'success_url': success_url,
            'fail_url': fail_url,
            'card_type': card_type,
            "order_id": random.randrange(1000),
            "amount": "1.00",
            "pan": TEST_CARD.get("pan"),
            "expiry": expirydate,
            "currency": currency,
            "success_url": "http://localhost:8000/success",
            "fail_url": "http://localhost:8000/success"
        }


class TestInit(TestThreeD):
    def test_initial_speed(self):
        self.assertEqual(0, 0)

    def test_start(self):
        data = self.three_d.prepare(**self.data)
        response = self.three_d.start()
        self.data = response
        result = xmltodict.parse(response)
        self.assertEqual(dict(result)['IPaySecure']['MessageErrorCode'], "200")

    def test_enrollment_result(self):
        self.three_d.prepare(**self.data)
        response = self.three_d.start()
        self.data = response
        result = self.three_d.enrollment_result()
        html_result = self.three_d.get_acs_html()
        with open("test.html", "w", encoding='utf-8') as file:
            file.write(str(html_result))
        print(result)

    def test_vpos_provision_request(self):
        pass
        # self.vpos.request_provision()
