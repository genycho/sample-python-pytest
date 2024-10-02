#-*- coding: utf-8 -*-
import os, sys, io
import pytest
from basic.calculator import calculator_machine
from common.exceptions import CalculateException

class TestCalculator:
    """ Test class for Calculator class
    """
    class_variable = "hello~ world~"

    def test_sum_basic(self):
        """ 테스트 목적 : 덧셈 기본확인 """
        target = calculator_machine()
        a = 2
        b = 7
        result = target.sum(a,b)
        assert 9 == result
        assert "hello~ world~" == self.class_variable

    def test_sum_floatvalue(self):
        """ 테스트 목적 : 실수(소수점)에 대한 덧셈 시도 """
        target = calculator_machine()
        a = 2.2
        b = 7.1
        with pytest.raises(CalculateException) as float_error:
            target.sum(a,b)
        assert 'only int type is allowed' == str(float_error.value)


    def test_sub_basic(self):
        """ 테스트 목적 : 뺄셈 기본확인 """
        target = calculator_machine()
        a = 2
        b = 7
        result = target.subtract(a,b)
        assert -5 == result


    def test_multiply_basic(self):
        """ 테스트 목적 : 곱셈 기본확인 """
        target = calculator_machine()
        a = 2
        b = 7
        result = target.multiply(a,b)
        assert 14 == result


    def test_divide_basic(self):
        """ 테스트 목적 : 나눗셈 기본확인 """
        target = calculator_machine()
        a = 90
        b = 30
        result = target.divide(a,b)
        assert 3 == result


    def test_divide_with0(self):
        """ 테스트 목적 : 0으로 나누기 시도 """
        target = calculator_machine()
        a = 10
        b = 0
        with pytest.raises(CalculateException) as dividezero_error:
            target.divide(a,b)
        assert 'only int type is allowed' == str(dividezero_error.value)
        assert 'cannot divide with zero' == str(dividezero_error.value)


    def test_divide_0withany(self):
        """ 테스트 목적 : 0을 나누기 시도 """
        target = calculator_machine()
        a = 0
        b = 10
        result = target.divide(a,b)
        assert 0 == result


# def test_sum_minusvalue():
#     """ 테스트 목적 : 음수에 대한 덧셈 시도 """

