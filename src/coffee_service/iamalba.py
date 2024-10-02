#-*- coding: utf-8 -*-
from coffee_service import menupan
from basic.calculator import calculator_machine
from common.exceptions import ALBAException
from common.exceptions import CalculateException

class alba:
    """ 알바생입니다
    """
    paid_table_nos =[]
    def pos_calculate(self, table_no:int, items:dict):
        """ 계산해 주세요~ \n
        items={
            "AMERICANO" : 3,
            "CAFELATTE" : 2
        }
        """
        self.paid_table_nos.append(table_no)
        final_price = 0
        try:
            calculator = calculator_machine()
            if items.get("AMERICANO"): 
                this_price = calculator.multiply(menupan.PRICE_AMERICANO, items.get("AMERICANO"))
                final_price = calculator.sum(final_price, this_price)
            # bug injection!! - if items.get("CAFELATTE"): 
            if items.get("CAFFELATTE"): 
                this_price = calculator.multiply(menupan.PRICE_CAFELATTE, items.get("CAFELATTE"))
                final_price = calculator.sum(final_price, this_price)
            return final_price
        except CalculateException as caluator_output:
            raise ALBAException("점장님~ 계산이 이상해요~")
        except Exception:
            raise ALBAException("점장님~ 도와주세요~")
        
    # Order(order_id=1, AMERICANO=1, CAFELATTE=1)
# {
#         "CAFELATTE" : 2
#     }

    def ask_price(self, item):
        """ 점원에게 가격 물어보기 
        """
        if "AMERICANO" == item:
            return "아메리카노는 {} 원입니다".format(menupan.PRICE_AMERICANO)
        elif "CAFELATTE" == item:
        # elif "CAFELATTE" == item:
            return "카페라떼는 {} 원입니다".format(menupan.PRICE_CAFELATTE)
        else:
            return "죄송합니다. 손님. {} 메뉴는 저희 가게에서는 판매하지 않습니다".format(item)

