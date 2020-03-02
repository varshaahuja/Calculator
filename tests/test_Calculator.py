from static_calc import calculator
import pytest
import unittest


class test_StaticCalc(unittest.TestCase):

    def test_calc(self):
        assert calculator

    def test_calc_addition(self):
        assert calculator.add(10.2, 2.5) == 12.7

    def test_calc_subtraction(self):
        assert calculator.sub(14, 10) == 4

    def test_calc_multiplication(self):
        assert calculator.multiply(3, 2) == 6

    def test_calc_division(self):
        assert calculator.div(12, 5) == 2.4

    def test_calc_square(self):
        assert calculator.square(13)== 169

    def test_calc_squareroot(self):
        assert calculator.squareroot(225) == 15