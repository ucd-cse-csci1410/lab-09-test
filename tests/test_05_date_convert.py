"""
test_04_split_date.py

Author: Chiranth Ajjamane Manohar
Date: 2026-02-05
Version: 0.1
Description: test file for the split_date function.
Copyright (c) 2026 University of Colorado Denver - Department of Computer Science

"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.part_02 import date_convert

# def date_convert (date_short):

#     #Use split_date function to get the mm, dd, and yyyy values
#     month, day, year = split_date (date_short)

#     # Use the month_to_name to convert month number to month name
#     month_name = month_to_name(month)

#     #Create date in long format
#     date_long = month_name + ' ' + day + ', ' + year

#     return date_long

class TestDateConvert(unittest.TestCase):
    """Unit tests for date_convert: converts short date into long date."""

    # case_01: Test short date 01/01/2026 to long date January 01, 2026
    def test_01_date_convert(self):
        """Test that date_convert converts short date 01/01/2026 to long date January 01, 2026."""
        date_short = '01/01/2026'
        expected_output = 'January 01, 2026'
        actual_output = date_convert(date_short)
        self.assertEqual(actual_output, expected_output, msg="Wrong date conversion. Expected 'January 01, 2026' for '01/01/2026'. Make sure your returning the correct long date.")

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestDateConvert))
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)