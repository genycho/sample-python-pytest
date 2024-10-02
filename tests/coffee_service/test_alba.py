#-*- coding: utf-8 -*-
import os, sys, io
import pytest
from coffee_service.iamalba import alba

def test_alba_poscalculate_basic():
    """ 테스트 목적 : 기본계산 확인 - 아메리카노 3개, 카페라떼 2개 """
    target = alba()
    purchased_drinks={
        "AMERICANO" : 3,
        "CAFELATTE" : 2
    }
    result = target.pos_calculate(2,purchased_drinks)
    assert 22000 == result

def test_alba_poscalculate_onlylatte():
    """ 테스트 목적 : 기본계산 확인 - 아메리카노 3개, 카페라떼 2개 """
    target = alba()
    purchased_drinks={
        "CAFELATTE" : 2
    }
    result = target.pos_calculate(2,purchased_drinks)
    assert 10000 == result

def test_alba_poscalculate_minus():
    """ 테스트 목적: 라떼를 하나 빼달라고 했을 때 어떻게 하는지 확인 """
    target = alba()
    purchased_drinks={
        "CAFELATTE" : -1
    }
    result = target.pos_calculate(2,purchased_drinks)
    assert -5000 == result


