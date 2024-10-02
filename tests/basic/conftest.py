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
