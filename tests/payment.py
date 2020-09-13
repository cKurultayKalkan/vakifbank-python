import unittest
import random
from vakifbank.ThreeD_Payment import ThreeDPayment
from tests.test_cards import TEST_CARD
from vakifbank.consts import CARD_TYPES, CURRENCY_TYPES
import xmltodict


class TestThreeD(unittest.TestCase):
    def setUp(self):
        year = TEST_CARD.get('expire_year')
        month = TEST_CARD.get('expire_month')
        expirydate = year[2:] + month
        currency = CURRENCY_TYPES.get(TEST_CARD.get("currency"))

        self.three_d = ThreeDPayment()
        self.data = {
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
        response = self.three_d.start(data)
        self.data = response
        result = xmltodict.parse(response)
        self.assertEqual(dict(result)['IPaySecure']['MessageErrorCode'], "200")

    def test_enrollment_result(self):
        data = self.three_d.prepare(**self.data)
        response = self.three_d.start(data)
        self.data = response
        result = self.three_d.enrollment_result(self.data)
        html_result = result.get('template')
        with open("test.html", "w", encoding='utf-8') as file:
            file.write(str(html_result))
        print(result)
