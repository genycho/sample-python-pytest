#-*- coding: utf-8 -*-
import os, sys, io
import pytest
from fastapi.testclient import TestClient
from coffee_restservice.fastapi_server import app

client = TestClient(app)

def test_fastapiserver_askprice_americano():
    """ 테스트 목적 : 아메리카노, 카페라떼 가격 문의"""
    to_ask_item = "AMERICANO"
    response = client.get("/price", params = {"item":to_ask_item})
    assert 200 == response.status_code, response.text
    response_body = response.json()
    assert 'result' in response_body
    assert '아메리카노는 4000 원입니다' == response_body['result']


def test_fastapiserver_askprice_cafelatte():
    to_ask_item = "CAFELATTE"
    response = client.get("/price", params = {"item":to_ask_item})
    assert 200 == response.status_code, response.text
    response_body = response.json()
    assert 'result' in response_body
    assert '카페라떼는 5000 원입니다' == response_body['result']


def test_fastapiserver_askprice_notsellingitem():
    """ 테스트 목적 : 안 파는 음료 가격 문의 """
    to_ask_item = "CAPPUCCINO"
    response = client.get("/price", params = {"item":to_ask_item})
    assert 400 == response.status_code, response.text
    response_body = response.json()
    assert 'detail' in response_body
    assert '판매하지 않는 음료입니다' == response_body['detail']


def test_fastapiserver_order_basic():
    data = {
        "order_id" : 1,
        "AMERICANO" : 1,
        "CAFELATTE" : 1
    }
    response = client.post("/order", json = data)
    assert 201 == response.status_code, response.text
    response_body = response.json()
    assert 'result' in response_body
    assert '전체 가격은 9000원입니다' == response_body['result']
