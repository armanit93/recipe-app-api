from django.test import TestCase
from app.calc import add



class CalcTests(TestCase):

    def test_add_number(self):
        """Testign Add functionality in Calc"""
        self.assertEqual(add(3,8),11)


