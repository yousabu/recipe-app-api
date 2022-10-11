# Sample test
from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):
    # Test the calc module

    def test_add_number(self):
        # Test adding number together
        res = calc.add(5,6)
        self.assertEqual(res, 11)
    
    def test_subtract_numbers(self):
        res = calc.sutract(10,15)
        self.assertEqual(res,-5)