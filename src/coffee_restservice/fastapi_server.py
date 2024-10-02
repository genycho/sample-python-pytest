#-*- coding: utf-8 -*-
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fastapi
from fastapi import FastAPI, HTTPException
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from coffee_service.iamalba import alba
from common.exceptions import ALBAException

class Order(BaseModel):
    """ 주문 모델 """
    order_id:int
    AMERICANO:Optional[int]
    CAFELATTE:Optional[int]

app = FastAPI()
common_error_msg = "오류가 발생했습니다. 잠시만 기다려 주세요."
    
@app.get("/price", description="아이템의 가격을 문의합니다", status_code=200)
async def get_price(item:str="AMERICANO,CAFELATTE"):
    """ 쿼리파라미터로 item="AMERICANO" 등으로 가격을 묻습니다 
    """
    albasang = alba()
    if item not in ['AMERICANO', 'CAFELATTE']:
        raise HTTPException(status_code=400, detail="판매하지 않는 음료입니다")
    try:
        answer = albasang.ask_price(item)
        return _make_200_response(answer)
    except ALBAException as alba_saying:
        raise HTTPException(status_code=500, detail=str(alba_saying.value))
    except Exception as detail_chk:
        raise HTTPException(status_code=500, detail=common_error_msg)


@app.post("/order", description="주문하고 가격을 확인합니다", status_code=201) # GET 메소드로 가장 루트 url로 접속할 경우
async def order(order: Order): # root() 함수를 실행하고
    """ 주문하고 가격 확인
    """
    albasang = alba()
    try:
        order_detail = {
            "AMERICANO": order.AMERICANO,
            "LATTE": order.CAFELATTE
        }
        return _make_response(fastapi.status.HTTP_201_CREATED, "전체 가격은 {}원입니다".format(albasang.pos_calculate(order.order_id, order_detail)))
    except ALBAException as alba_saying:
        raise HTTPException(status_code=500, detail=str(alba_saying.value))
    except Exception as detail_chk:
        raise HTTPException(status_code=500, detail=common_error_msg)


@app.get("/order/{orderId}")
async def get_orderinfo(orderId:int):
    # albasang = alba()
    try:
       raise HTTPException(status_code=500, detail="not yet implemented.")
    except Exception:
       raise HTTPException(status_code=500, detail="not yet implemented.")
    

def _make_200_response(body_text):
    return _make_response(fastapi.status.HTTP_200_OK, body_text)

def _make_response(status_code, body_text):
    return fastapi.responses.JSONResponse(
        status_code=status_code,
        content={"result" : body_text},
        headers={"content-type": "application/json"}
    )