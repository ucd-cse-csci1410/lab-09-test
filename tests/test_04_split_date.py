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
from src.part_02 import split_date

# def split_date (date_short):

#     # Use the split method to split short date into three
#     # parts: month, day, and year
#     month, day, year = date_short.split('/')

#     # Return month, day and year
#     return month, day, year

class TestSplitDate(unittest.TestCase):
    """Unit tests for split_date: splits short date into month, day and year."""

    # case_01: Test month number 1 to month name January
    def test_01_split_date(self):
        """Test that split_date splits short date into month, day and year."""
        self.assertEqual(split_date('01/01/2026'), ('01', '01', '2026'), msg="Wrong split date. Expected ('01', '01', '2026') for '01/01/2026'. Make sure your returning the correct month, day and year.")

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestSplitDate))
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)