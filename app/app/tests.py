from django.test import TestCase
from app.calc import add, subtract



class CalcTests(TestCase):

    def test_add_number(self):
        """Testign Add functionality in Calc"""
        self.assertEqual(add(3,8),11)


    def test_subtract_number(self):
    	"""Testing Subtract Functionality in Calc """
    	self.assertEqual(subtract(8,3),5)


