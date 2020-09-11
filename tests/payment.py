import unittest
from vakifbank.ThreeD_Payment import ThreeDPayment


class TestThreeD(unittest.TestCase):
    def setUp(self):
        self.three_d = ThreeDPayment()


class TestInit(TestThreeD):
    def test_initial_speed(self):
        self.assertEqual(0, 0)
