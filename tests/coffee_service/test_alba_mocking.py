#-*- coding: utf-8 -*-
import os, sys, io
import pytest
from coffee_service.iamalba import alba
from coffee_service import menupan
from basic.calculator import calculator_machine
from common.exceptions import ALBAException
from common.exceptions import CalculateException

def test_alba_poscalculate_basic(mocker):
    """ 테스트 목적: 계산기 핑계를 대는 알바생에게 바로 계산해보라고 시키기 """
    target = alba()
    purchased_drinks={
        "AMERICANO" : 3,
        "CAFELATTE" : 2
    }
    # mocker.spy(calculator_machine, "multiply")
    mocker.patch("basic.calculator.calculator_machine.multiply", return_value=10000)    #4000, 5000
    mocker.patch("basic.calculator.calculator_machine.sum", return_value=22000)    #4000, 5000
    result = target.pos_calculate(2,purchased_drinks)
    assert 22000 == result


def test_alba_poscalculate_calculatorerror(mocker):
    """ 테스트 목적: 계산기가 임의로 0원으로 잘못계산될 때 알바생의 동작을 확인 """
    target = alba()
    purchased_drinks={
        "AMERICANO" : 3,
        "CAFELATTE" : 2
    }
    mocker.patch("basic.calculator.calculator_machine.sum", return_value="0")
    with pytest.raises(ALBAException) as expected_saying:
        target.pos_calculate(2,purchased_drinks)
    assert "잠시만 기다려 주세요. 계산 오류가 있습니다" == str(expected_saying.value)


def test_alba_poscalculate_calculatorerror(mocker):
    """ 테스트 목적: 계산기가 임의로 CalculateException 발생할 때 알바생의 동작을 확인 """
    target = alba()
    purchased_drinks={
        "AMERICANO" : 3,
        "CAFELATTE" : 2
    }
    mocker.patch("basic.calculator.calculator_machine.sum", side_effect=CalculateException("계산기오류입니다"))
    with pytest.raises(ALBAException) as expected_saying:
        target.pos_calculate(2,purchased_drinks)
    assert "점장님~ 계산이 이상해요~" == str(expected_saying.value)



def test_alba_askprice_basic(mocker):
    """ 테스트 목적: 가격 물어보기. 이미 정의된 상수 값을 임의로 조작한 후 확인하는 예제  
    """
    to_ask_beverage = "CAFELATTE"
    target = alba()
    from coffee_service import menupan
    mocker.patch.object(menupan, "PRICE_CAFELATTE", 10000)
    answer_price = target.ask_price(to_ask_beverage)
    assert '카페라떼는 10000 원입니다' == answer_price


