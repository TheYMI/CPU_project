#!/usr/bin/python
"""
bit_value.py

Created by Yuval Tzur on 15/12/2015.
"""

import unittest
from bit_value import BitValue


class BitValueConstructorTests(unittest.TestCase):
    """ This is a unit test class for the constructor of the BitValue class """

    def test_default_constructor(self):
        bv = BitValue()
        self.assertEqual(str(bv), "0000000000000000")

    def test_constructor_int_value(self):
        bv = BitValue(10)
        self.assertEqual(str(bv), "0000000000001010")

    def test_constructor_int_value_base_10(self):
        bv = BitValue(10, base=10)
        self.assertEqual(str(bv), "0000000000001010")

    def test_constructor_str_value_base_10(self):
        bv = BitValue("10", base=10)
        self.assertEqual(str(bv), "0000000000001010")

    def test_constructor_int_value_base_int(self):
        bv = BitValue(10, base="int")
        self.assertEqual(str(bv), "0000000000001010")

    def test_constructor_str_value_base_int(self):
        bv = BitValue("10", base="int")
        self.assertEqual(str(bv), "0000000000001010")

    def test_constructor_int_value_base_2(self):
        bv = BitValue(10, base=2)
        self.assertEqual(str(bv), "0000000000000010")

    def test_constructor_str_value_base_2(self):
        bv = BitValue("10", base=2)
        self.assertEqual(str(bv), "0000000000000010")

    def test_constructor_int_value_base_bin(self):
        bv = BitValue(10, base="bin")
        self.assertEqual(str(bv), "0000000000000010")

    def test_constructor_str_value_base_bin(self):
        bv = BitValue("10", base="bin")
        self.assertEqual(str(bv), "0000000000000010")

    def test_constructor_int_value_base_16(self):
        bv = BitValue(10, base=16)
        self.assertEqual(str(bv), "0000000000010000")

    def test_constructor_str_value_base_16(self):
        bv = BitValue("10", base=16)
        self.assertEqual(str(bv), "0000000000010000")

    def test_constructor_int_value_base_hex(self):
        bv = BitValue(10, base="hex")
        self.assertEqual(str(bv), "0000000000010000")

    def test_constructor_str_value_base_hex(self):
        bv = BitValue("10", base="hex")
        self.assertEqual(str(bv), "0000000000010000")

    def test_constructor_int_value_base_5(self):
        bv = BitValue(10, base=5)
        self.assertEqual(str(bv), "0000000000000101")

    def test_constructor_str_value_base_5(self):
        bv = BitValue("10", base=5)
        self.assertEqual(str(bv), "0000000000000101")

    def test_constructor_legal_value_size_4(self):
        bv = BitValue(15, size=4)
        self.assertEqual(str(bv), "1111")

    def test_constructor_overflow_value_size_4(self):
        bv = BitValue(16, size=4)
        self.assertEqual(str(bv), "0000")

    def test_negative_value(self):
        bv = BitValue(-4)
        self.assertEqual(str(bv), "1111111111111100")


class BitValueComparisonTests(unittest.TestCase):
    """ This is a unit test class for the comparison operators of the BitValue class """

    def setUp(self):
        self.bv1 = BitValue(2, size=4)
        self.bv2 = BitValue(3, size=4)
        self.bv3 = BitValue(4, size=4)
        self.bv4 = BitValue(4, size=4)
        self.bv5 = BitValue(0, size=4)
        self.bv6 = BitValue(-1, size=4)
        self.bv7 = BitValue(-2, size=4)

    def tearDown(self):
        self.bv1 = None
        self.bv2 = None
        self.bv3 = None
        self.bv4 = None
        self.bv5 = None
        self.bv6 = None
        self.bv7 = None

    # Less than (<):
    def test_2_less_than_3(self):
        self.assertTrue(self.bv1 < self.bv2)

    def test_3_less_than_2(self):
        self.assertFalse(self.bv2 < self.bv1)

    def test_4_less_than_4(self):
        self.assertFalse(self.bv3 < self.bv4)

    def test_negative_2_less_than_0(self):
        self.assertTrue(self.bv7 < self.bv5)

    def test_negative_2_less_than_negative_1(self):
        self.assertTrue(self.bv7 < self.bv6)

    def test_negative_1_less_than_negative_2(self):
        self.assertFalse(self.bv6 < self.bv7)

    def test_negative_1_less_than_negative_1(self):
        self.assertFalse(self.bv6 < self.bv6)

    def test_negative_1_less_than_2(self):
        self.assertTrue(self.bv6 < self.bv1)

    # Less or equal to (<=):
    def test_2_less_or_equal_to_3(self):
        self.assertTrue(self.bv1 <= self.bv2)

    def test_3_less_or_equal_to_2(self):
        self.assertFalse(self.bv2 <= self.bv1)

    def test_4_less_or_equal_to_4(self):
        self.assertTrue(self.bv3 <= self.bv4)

    def test_negative_2_less_or_equal_to_0(self):
        self.assertTrue(self.bv7 <= self.bv5)

    def test_negative_2_less_or_equal_to_negative_1(self):
        self.assertTrue(self.bv7 <= self.bv6)

    def test_negative_1_less_or_equal_to_negative_2(self):
        self.assertFalse(self.bv6 <= self.bv7)

    def test_negative_1_less_or_equal_to_negative_1(self):
        self.assertTrue(self.bv6 <= self.bv6)

    def test_negative_1_less_or_equal_to_2(self):
        self.assertTrue(self.bv6 <= self.bv1)

    # Equal to (==):
    def test_2_equal_to_3(self):
        self.assertFalse(self.bv1 == self.bv2)

    def test_4_equal_to_4(self):
        self.assertTrue(self.bv3 == self.bv4)

    def test_negative_2_equal_to_0(self):
        self.assertFalse(self.bv7 == self.bv5)

    def test_negative_1_equal_to_negative_1(self):
        self.assertTrue(self.bv6 == self.bv6)

    # Not equal to (!=):
    def test_2_not_equal_to_3(self):
        self.assertTrue(self.bv1 != self.bv2)

    def test_4_not_equal_to_4(self):
        self.assertFalse(self.bv3 != self.bv4)

    def test_negative_2_not_equal_to_0(self):
        self.assertTrue(self.bv7 != self.bv5)

    def test_negative_1_not_equal_to_negative_1(self):
        self.assertFalse(self.bv6 != self.bv6)

    # Greater or equal to (>=):
    def test_2_greater_or_equal_to_3(self):
        self.assertFalse(self.bv1 >= self.bv2)

    def test_3_greater_or_equal_to_2(self):
        self.assertTrue(self.bv2 >= self.bv1)

    def test_4_greater_or_equal_to_4(self):
        self.assertTrue(self.bv3 >= self.bv4)

    def test_negative_2_greater_or_equal_to_0(self):
        self.assertFalse(self.bv7 >= self.bv5)

    def test_negative_2_greater_or_equal_to_negative_1(self):
        self.assertFalse(self.bv7 >= self.bv6)

    def test_negative_1_greater_or_equal_to_negative_2(self):
        self.assertTrue(self.bv6 >= self.bv7)

    def test_negative_1_greater_or_equal_to_negative_1(self):
        self.assertTrue(self.bv6 >= self.bv6)

    def test_negative_1_greater_or_equal_to_2(self):
        self.assertFalse(self.bv6 >= self.bv1)

    # Greater than (>):
    def test_2_greater_than_3(self):
        self.assertFalse(self.bv1 > self.bv2)

    def test_3_greater_than_2(self):
        self.assertTrue(self.bv2 > self.bv1)

    def test_4_greater_than_4(self):
        self.assertFalse(self.bv3 > self.bv4)

    def test_negative_2_greater_than_0(self):
        self.assertFalse(self.bv7 > self.bv5)

    def test_negative_2_greater_than_negative_1(self):
        self.assertFalse(self.bv7 > self.bv6)

    def test_negative_1_greater_than_negative_2(self):
        self.assertTrue(self.bv6 > self.bv7)

    def test_negative_1_greater_than_negative_1(self):
        self.assertFalse(self.bv6 > self.bv6)

    def test_negative_1_greater_than_2(self):
        self.assertFalse(self.bv6 > self.bv1)


class BitValueArithmeticTests(unittest.TestCase):
    """ This is a unit test class for the arithmetic operators of the BitValue class """

    def setUp(self):
        self.bv1 = BitValue(1, size=8)
        self.bv2 = BitValue(2, size=8)
        self.bv3 = BitValue(3, size=8)
        self.bv4 = BitValue(-2, size=8)
        self.bv5 = BitValue(0, size=8)

    def tearDown(self):
        self.bv1 = None
        self.bv2 = None
        self.bv3 = None
        self.bv4 = None
        self.bv5 = None

    # Absolute:
    def test_absolute_2(self):
        self.assertEqual(abs(self.bv2), 2)

    def test_absolute_negative_2(self):
        self.assertEqual(abs(self.bv4), 2)

    # Negative (-<BV>):
    def test_negative_2(self):
        self.assertEqual(-self.bv2, -2)

    def test_negative_negative_2(self):
        self.assertEqual(-self.bv4, 2)

    # Positive (+<BV>):
    def test_positive_2(self):
        self.assertEqual(+self.bv2, 2)

    def test_positive_negative_2(self):
        self.assertEqual(+self.bv4, -2)

    # Addition (<BV> + <BV>):
    def test_add_positive_positive(self):
        self.assertEqual(self.bv1 + self.bv2, 3)

    def test_add_positive_negative(self):
        self.assertEqual(self.bv1 + self.bv4, -1)

    def test_add_negative_positive(self):
        self.assertEqual(self.bv4 + self.bv3, 1)

    def test_add_negative_negative(self):
        self.assertEqual(self.bv4 + self.bv4, -4)

    def test_add_positive_zero(self):
        self.assertEqual(self.bv1 + self.bv5, 1)

    def test_add_negative_zero(self):
        self.assertEqual(self.bv4 + self.bv5, -2)

    # Subtraction (<BV> - <BV>):
    def test_sub_positive_positive(self):
        self.assertEqual(self.bv1 - self.bv2, -1)

    def test_sub_positive_negative(self):
        self.assertEqual(self.bv1 - self.bv4, 3)

    def test_sub_negative_positive(self):
        self.assertEqual(self.bv4 - self.bv3, -5)

    def test_sub_negative_negative(self):
        self.assertEqual(self.bv4 - self.bv4, 0)

    def test_sub_positive_zero(self):
        self.assertEqual(self.bv1 - self.bv5, 1)

    def test_sub_negative_zero(self):
        self.assertEqual(self.bv4 - self.bv5, -2)

    # Multiplication (<BV> * <BV>):
    def test_mul_positive_positive(self):
        self.assertEqual(self.bv1 * self.bv2, 2)

    def test_mul_positive_negative(self):
        self.assertEqual(self.bv1 * self.bv4, -2)

    def test_mul_negative_positive(self):
        self.assertEqual(self.bv4 * self.bv3, -6)

    def test_mul_negative_negative(self):
        self.assertEqual(self.bv4 * self.bv4, 4)

    def test_mul_positive_zero(self):
        self.assertEqual(self.bv1 * self.bv5, 0)

    def test_mul_negative_zero(self):
        self.assertEqual(self.bv4 * self.bv5, 0)

    # Modulo (<BV> % <BV>):
    def test_mod_positive_positive(self):
        self.assertEqual(self.bv3 % self.bv2, 1)

    def test_mod_positive_negative(self):
        self.assertEqual(self.bv3 % self.bv4, -1)

    def test_mod_negative_positive(self):
        self.assertEqual(self.bv4 % self.bv3, 1)

    def test_mod_negative_negative(self):
        self.assertEqual(self.bv4 % self.bv4, 0)

    def test_mod_positive_zero(self):
        self.assertRaises(ZeroDivisionError, lambda: self.bv1 % self.bv5)

    def test_mod_negative_zero(self):
        self.assertRaises(ZeroDivisionError, lambda: self.bv4 % self.bv5)

    def test_mod_zero_positive(self):
        self.assertEqual(self.bv5 % self.bv1, 0)

    def test_mod_zero_negative(self):
        self.assertEqual(self.bv5 % self.bv4, 0)

    # Division (<BV> / <BV>):
    def test_div_positive_positive(self):
        self.assertEqual(self.bv3 / self.bv2, 1)

    def test_div_positive_negative(self):
        self.assertEqual(self.bv3 / self.bv4, -2)

    def test_div_negative_positive(self):
        self.assertEqual(self.bv4 / self.bv1, -2)

    def test_div_negative_negative(self):
        self.assertEqual(self.bv4 / self.bv4, 1)

    def test_div_positive_zero(self):
        self.assertRaises(ZeroDivisionError, lambda: self.bv1 / self.bv5)

    def test_div_negative_zero(self):
        self.assertRaises(ZeroDivisionError, lambda: self.bv4 / self.bv5)

    def test_div_zero_positive(self):
        self.assertEqual(self.bv5 / self.bv1, 0)

    def test_div_zero_negative(self):
        self.assertEqual(self.bv5 / self.bv4, 0)

    # Floor division (<BV> // <BV>):
    def test_floordiv_positive_positive(self):
        self.assertEqual(self.bv3 // self.bv2, 1)

    def test_floordiv_positive_negative(self):
        self.assertEqual(self.bv3 // self.bv4, -2)

    def test_floordiv_negative_positive(self):
        self.assertEqual(self.bv4 // self.bv1, -2)

    def test_floordiv_negative_negative(self):
        self.assertEqual(self.bv4 // self.bv4, 1)

    def test_floordiv_positive_zero(self):
        self.assertRaises(ZeroDivisionError, lambda: self.bv1 // self.bv5)

    def test_floordiv_negative_zero(self):
        self.assertRaises(ZeroDivisionError, lambda: self.bv4 // self.bv5)

    def test_floordiv_zero_positive(self):
        self.assertEqual(self.bv5 // self.bv1, 0)

    def test_floordiv_zero_negative(self):
        self.assertEqual(self.bv5 // self.bv4, 0)

    # Power (<BV> ** <BV>):
    def test_pow_positive_positive(self):
        self.assertEqual(self.bv3 ** self.bv2, 9)

    def test_pow_negative_positive(self):
        self.assertEqual(self.bv4 ** self.bv1, -2)

    def test_pow_positive_zero(self):
        self.assertEqual(self.bv1 ** self.bv5, 1)

    def test_pow_negative_zero(self):
        self.assertEqual(self.bv4 ** self.bv5, 1)

    def test_pow_zero_positive(self):
        self.assertEqual(self.bv5 ** self.bv1, 0)

    def test_pow_negative_exponent(self):
        self.assertRaises(ValueError, lambda: self.bv5 ** self.bv4)


if __name__ == "__main__":
    suites = {"constructor": {"tests": unittest.TestLoader().loadTestsFromTestCase(BitValueConstructorTests), "verbosity": 0},
              "comparison": {"tests": unittest.TestLoader().loadTestsFromTestCase(BitValueComparisonTests), "verbosity": 0},
              "arithmetic": {"tests": unittest.TestLoader().loadTestsFromTestCase(BitValueArithmeticTests), "verbosity": 0}}

    for suite in suites.values():
        unittest.TextTestRunner(verbosity=suite["verbosity"]).run(suite["tests"])
