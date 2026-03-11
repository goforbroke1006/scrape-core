from fractions import Fraction
from unittest import TestCase

from scrape_core.contract.prime.currency.currency_code import Currency3Code
from scrape_core.contract.prime.price.parser import parse


class Test(TestCase):
    def test_parse_usual_amount_with_3letter_code(self):
        pi = parse('1,234.56 USD')
        self.assertIsNotNone(pi)
        self.assertEqual(pi.text, '1,234.56 USD')
        self.assertEqual(pi.amount, Fraction('1234.56'))
        self.assertEqual(pi.currency, Currency3Code.UnitedStatesDollar)
    
    def test_parse_avezor_ge(self):
        pi = parse('314,600 ₾')
        self.assertIsNotNone(pi)
        self.assertEqual(pi.text, '314,600 ₾')
        self.assertEqual(pi.amount, Fraction('314600'))
        self.assertEqual(pi.currency, Currency3Code.GeorgianLari)
