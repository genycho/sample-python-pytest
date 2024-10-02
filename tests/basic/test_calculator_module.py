#-*- coding: utf-8 -*-
import os, sys, io
import pytest
from basic.calculator import calculator_machine
from common.exceptions import CalculateException

@pytest.fixture(scope="function")
def get_caculator():
    calc = calculator_machine()
    calc.reset()
    # return calc
    yield calc
    # "테스트가 완료되면 yield문 이후 코드가 실행됩니다"

def test_sum_basic(get_caculator):
    """ 테스트 목적 : 덧셈 기본확인 """
    target = get_caculator
    a = 2
    b = 7
    result = target.sum(a,b)
    assert 9 == result, "테스트가 실패했습니다. 기대한 결과와 다른 결과 값이 나왔습니다 - " + str(result)

@pytest.mark.skip(reason="이 테스트는 skip합니다")
def test_sum_floatvalue(get_caculator):
    """ 테스트 목적 : 실수(소수점)에 대한 덧셈 시도 """
    target = get_caculator
    a = 2.2
    b = 7.1
    with pytest.raises(CalculateException) as float_error:
        target.sum(a,b)
    assert 'only int type is allowed' == str(float_error.value)

@pytest.mark.prod
def test_sub_basic():
    """ 테스트 목적 : 뺄셈 기본확인 """
    target = calculator_machine()
    a = 2
    b = 7
    result = target.subtract(a,b)
    assert -5 == result


def test_multiply_basic():
    """ 테스트 목적 : 곱셈 기본확인 """
    target = calculator_machine()
    a = 2
    b = 7
    result = target.multiply(a,b)
    assert 14 == result

def test_divide_basic():
    """ 테스트 목적 : 나눗셈 기본확인 """
    target = calculator_machine()
    a = 90
    b = 30
    result = target.divide(a,b)
    assert 3 == result


def test_divide_with0():
    """ 테스트 목적 : 0으로 나누기 시도 """
    target = calculator_machine()
    a = 10
    b = 0
    with pytest.raises(CalculateException) as dividezero_error:
        target.divide(a,b)
    assert 'only int type is allowed' == str(dividezero_error.value)


def test_divide_0withany():
    """ 테스트 목적 : 0을 나누기 시도 """
    target = calculator_machine()
    a = 0
    b = 10
    result = target.divide(a,b)
    assert 0 == result

@pytest.mark.parametrize("input_a,input_b,expected",{(10,2,12),(2,10,12),(5,5,10),(0,0,0)})
def test_sum_parameterizedtest(input_a, input_b, expected):
    """ 테스트 목적 : 덧셈에 대한 parameterized 테스트 예 """
    target = calculator_machine()
    a = input_a
    b = input_b
    assert expected == target.sum(a,b)


# def test_sum_minusvalue():
#     """ 테스트 목적 : 음수에 대한 덧셈 시도 """

# def test_sum_더큰b값(get_caculator):
#     target = calculator_machine()
#     a = 2
#     b = 7
#     assert 9 == target.sum(a,b)

