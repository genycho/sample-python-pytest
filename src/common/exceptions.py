#-*- coding: utf-8 -*-
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class CalculateException(Exception):
    """ a custom exception for error handling on test script level(not target side)"""
    def __init__(self, message):
        self.value = message

    def __str__(self):
        return self.value

class ALBAException(Exception):
    """ a custom exception for error handling on test script level(not target side)"""
    def __init__(self, message):
        self.value = message

    def __str__(self):
        return self.value

class MyTestException(Exception):
    """ a custom exception for error handling on test script level(not target side)"""
    def __init__(self, message):
        self.value = message

    def __str__(self):
        return self.value
