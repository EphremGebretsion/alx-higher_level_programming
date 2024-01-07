#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    test case class for max integer function
    it tests for result, negative numbers, empity list
    """

    def test_res(self):
        """
        result of posetive integers
        """
        self.assertAlmostEqual(max_integer([1, 2, 30, 5]), 30)

    def test_neg(self):
        """
        tests including negative numbers
        """
        self.assertAlmostEqual(max_integer([9, -23, 3]), 9)
        self.assertAlmostEqual(max_integer([-32, -389, -1]), -1)

    def test_emp(self):
        """
        tests the result of empty list
        """
        self.assertAlmostEqual(max_integer([]), None)
