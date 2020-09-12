import unittest
import random
from vakifbank.ThreeD_Payment import ThreeDPayment
from tests.test_cards import TEST_CARD
from vakifbank.consts import CARD_TYPES, CURRENCY_TYPES
import xmltodict


class TestThreeD(unittest.TestCase):
    def setUp(self):
        self.three_d = ThreeDPayment()


class TestInit(TestThreeD):
    def test_initial_speed(self):
        self.assertEqual(0, 0)

    def test_start(self):
        year = TEST_CARD.get('expire_year')
        month = TEST_CARD.get('expire_month')
        expirydate = year[2:] + month
        currency = CURRENCY_TYPES.get(TEST_CARD.get("currency"))

        req = {
            "order_id": random.randrange(1000),
            "amount": "1.00",
            "pan": TEST_CARD.get("pan"),
            "expiry": expirydate,
            "currency": currency,
            "success_url": "http://localhost:8000/success",
            "fail_url": "http://localhost:8000/success"
        }
        data = self.three_d.prepare(**req)
        response = self.three_d.start(data)
        result = xmltodict.parse(response)
        self.assertEqual(dict(result)['IPaySecure']['MessageErrorCode'], "200")
