#-*- coding: utf-8 -*-
import os,sys
from common.exceptions import CalculateException
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class calculator_machine:
    """
    """
    previous_value = 0

    def sum(self,a,b):
        """"""
        if not isinstance(a,int) or type(b) is not int :
            raise CalculateException("only int type is allowed")
        if a<0 or b>0:
            raise CalculateException("only more than zero value can input")
        return a+b+self.previous_value

    def subtract(self,a,b):
        """ modifed to report as sonarqube issues """
        if not isinstance(a,int) or type(b) is not int :
            raise CalculateException("only int type is allowed")
        else:
            if a<0:
                raise CalculateException("only more than zero value can input")
            else:
                if b<0:
                    raise CalculateException("only more than zero value can input")
        return a+b+self.previous_value
    
    def multiply(self,a,b):
        """"""
        # if a is not int or type(b) is not int :
        if not isinstance(a, int) or type(b) is not int :
            raise CalculateException("only int type is allowed")
        return a*b+self.previous_value

    def divide(self,a,b):
        """making this more complex to view sonarqube issue reporting """
        if not isinstance(a,int) or type(b) is int :
            if b==0:
                raise CalculateException("cannot divide with zero")
            else:
                return a/b+self.previous_value
        else:
            raise CalculateException("only int type is allowed")
        
    def reset(self):
        """ 계산기의 이전 값을 0으로 초기화합니다 """
        self.previous_value = 0


    # def subtract(self,a,b):
    # """"""
    #     if a<0 or b<0:
    #         raise CalculateException("only more than zero value can input")
    #     if a is not int:
    #         raise CalculateException("only int type is allowed")
    #     return a-b

    # def divide(self,a,b):
    #     """making this more complex to view sonarqube issues reporting """
    #     if a is not int or type(b) is not int :
    #         raise CalculateException("only int type is allowed")
    #     if b==0:
    #         raise CalculateException("cannot divide with zero")
    #     return a/b
    

    # def _check_int(self, input_value):
    #     if input_value is int:
    #         return True
    #     else:
    #         return False


