"""
test_01_f_to_c.py

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
from src.part_01 import f_to_c


class TestFToC(unittest.TestCase):
    """Unit tests for f_to_c: converts temperature in Fahrenheit to Celsius."""

    # case_01: 32 F should equal 0 C.
    def test_01_freezing_point(self):
        """32 F should equal 0 C."""
        #assertAlmostEqual(first, second, places=7, msg=None, delta=None)
        #places=3 means the difference between the two values should be less than 0.0001
        #example = 5.5556 and 5.5555 difference = 0.0001  rounding it to 3 places  = 0.000 which is equal to 0.0 test passes.
        self.assertAlmostEqual(f_to_c(32), 0.0, places=3, msg="Wrong converstion. Expected 0.0 for 32 F. Make sure your retunring the converted result from the function f_to_c.")

    # case_02: 212 F should equal 100 C.
    def test_02_boiling_point(self):
        """212 F should equal 100 C."""
        self.assertAlmostEqual(f_to_c(212), 100.0, places=3, msg="Wrong converstion. Expected 100.0 for 212 F.Make sure your retunring the converted result from the function f_to_c.")

    # case_03: 0 F should equal approximately -17.777... C.
    def test_03_zero_fahrenheit(self):
        """0 F should equal approximately -17.777... C."""
        self.assertAlmostEqual(f_to_c(0), -160 / 9, places=3, msg="Wrong converstion. Expected -17.777... for 0 F. Make sure your retunring the converted result from the function f_to_c.")

    # case_04: -40 F should equal -40 C.
    def test_04_negative_fahrenheit(self):
        """-40 F should equal -40 C."""
        self.assertAlmostEqual(f_to_c(-40), -40.0, places=3, msg="Wrong converstion. Expected -40.0 for -40 F. Make sure your retunring the converted result from the function f_to_c.")

    # case_05: 98.6 F should equal 37 C.
    def test_05_float_input(self):
        """98.6 F (body temp) should convert correctly."""
        self.assertAlmostEqual(f_to_c(98.6), 37.0, places=3, msg="Wrong converstion. Expected 37.0 for 98.6 F. Make sure your retunring the converted result from the function f_to_c.")



if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestFToC))
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)