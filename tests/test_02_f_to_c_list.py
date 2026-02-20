"""
test_01_f_to_c_list.py

Author: Chiranth Ajjamane Manohar
Date: 2026-02-05
Version: 0.1
Description: test file for the f_to_c and f_to_c_list functions.
Copyright (c) 2026 University of Colorado Denver - Department of Computer Science

"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.part_01 import f_to_c_list


# def f_to_c_list(temp_list):
#     for i in range(len(temp_list)):
#         fahrenheit = temp_list[i]
#         celsius = f_to_c (fahrenheit)
#         temp_list[i] = round(celsius,2)



class TestFToCList(unittest.TestCase):
    """Unit tests for f_to_c_list: converts temperature in Fahrenheit to Celsius. Pop them in templist"""

    # case_01: Test list conversion [32, 212, 0, -40, 98.6] to Celsius
    def test_01_list_conversion(self):
        """Test that f_to_c_list converts [32, 212, 0, -40, 98.6] F to Celsius correctly."""
        temp_list = [32, 212, 0, -40, 98.6]
        expected_output = [0.0, 100.0, -17.78, -40.0, 37.0]
        
        f_to_c_list(temp_list)
        
        # Check that each element matches expected value (rounded to 2 decimal places)
        self.assertEqual(len(temp_list), len(expected_output), 
                        msg="List length should remain the same after conversion.")
        
        for i, (actual, expected) in enumerate(zip(temp_list, expected_output)):
            self.assertEqual(actual, expected,
                                  msg=f"Wrong conversion at index {i}. Expected {expected}, got {actual}. Make sure f_to_c_list is converting and rounding correctly.")


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestFToCList))
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)