#-*- coding: utf-8 -*-
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
import uuid
import datetime
from datetime import datetime as dt
from common.exceptions import MyTestException

        
########### COMMON ###########
def get_uuid():
    return uuid.uuid4()

############### FILE ################
def open_json_file(filepath):
    with open(filepath) as json_file:
        _json_body = json.load(json_file)
        json_file.close()
    return _json_body

def get_file_binary(filepath):
    with open(filepath, 'rb') as f:
        result = f.read()
        f.close()
    return result

def write_file_text(filepath, text_data):
    with open(filepath, "w") as f:
        f.write(text_data)
        print("file write succeded")
        f.close()
    return True

def write_file_binary(filepath, binary_data):
    with open(filepath, "wb") as f:
        f.write(bytes(binary_data))
        # f.write(binary_data)
        print("file write succeded")
        f.close()
    return True

############### DATETIME ################
def _get_curdatetime_wformat(format):
    gen_value = dt.now().strftime(format)
    return gen_value

def get_curdate():
    return _get_curdatetime_wformat('%Y%m%d')    

def get_curdatetime():
    return _get_curdatetime_wformat('%Y%m%d_%H%M%S')

def get_curdatetime_millisec():
    return _get_curdatetime_wformat('%Y%m%d%H%M%S%f')


