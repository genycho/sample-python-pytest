#-*- coding: utf-8 -*-
import os, sys, io
import unittest
from basic.calculator import calculator_machine
from common.exceptions import CalculateException


class CalculatorTest(unittest.TestCase):
    def test_sum_bigger_b(self):
        target = calculator_machine()
        a = 2
        b = 7
        self.assertEqual(9, target.sum(a,b))























