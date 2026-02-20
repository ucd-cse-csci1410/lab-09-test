"""
test_03_month_to_name.py

Author: Chiranth Ajjamane Manohar
Date: 2026-02-05
Version: 0.1
Description: test file for the f_to_c and f_to_c_list functions.
Copyright (c) 2026 University of Colorado Denver - Department of Computer Science

"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.part_02 import month_to_name

# def month_to_name (month):

#     #Use a list to store name of the months
#     #using using line continuation to avoid going of the screen edge
#     month_list = ['January', 'February', 'March', \
#                 'April', 'May', 'June',         \
#                 'July', 'August', 'September',  \
#                 'October', 'November', 'December']

#     month_name = month_list[int(month)-1]

#     return month_name

class TestMonthToName(unittest.TestCase):
    """Unit tests for month_to_name: converts month number to month name."""

    # case_01: Test month number 1 to month name January
    def test_01_month_to_name(self):
        """Test that month_to_name converts month number 1 to month name January."""
        self.assertEqual(month_to_name(1), 'January', msg="Wrong month name. Expected January for month number 1. Check spelling and case of the month name.")
        self.assertEqual(month_to_name(2), 'February', msg="Wrong month name. Expected February for month number 2. Check spelling and case of the month name.")    
        self.assertEqual(month_to_name(3), 'March', msg="Wrong month name. Expected March for month number 3. Check spelling and case of the month name.")
        self.assertEqual(month_to_name(4), 'April', msg="Wrong month name. Expected April for month number 4. Check spelling and case of the month name.")
        self.assertEqual(month_to_name(5), 'May', msg="Wrong month name. Expected May for month number 5. Check spelling and case of the month name.")
        self.assertEqual(month_to_name(6), 'June', msg="Wrong month name. Expected June for month number 6. Check spelling and case of the month name.")
        self.assertEqual(month_to_name(7), 'July', msg="Wrong month name. Expected July for month number 7. Check spelling and case of the month name.")
        self.assertEqual(month_to_name(8), 'August', msg="Wrong month name. Expected August for month number 8. Check spelling and case of the month name.")
        self.assertEqual(month_to_name(9), 'September', msg="Wrong month name. Expected September for month number 9. Check spelling and case of the month name.") 
        self.assertEqual(month_to_name(10), 'October', msg="Wrong month name. Expected October for month number 10. Check spelling and case of the month name." )
        self.assertEqual(month_to_name(11), 'November', msg="Wrong month name. Expected November for month number 11. Check spelling and case of the month name.")
        self.assertEqual(month_to_name(12), 'December', msg="Wrong month name. Expected December for month number 12. Check spelling and case of the month name.")

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestMonthToName))
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)