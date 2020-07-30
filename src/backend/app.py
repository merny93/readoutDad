"""
Application stub
"""
import sys
import time
import random ##for fake data gen




params = {
    'name':10,
    'value': 20,
    'stuff': 30
}

monitor_vals = {
    'voltage': 0,
    'current': 0
}


def initialize():
    #will run everytime any page loads
    pass
    return True



def serial_connection():
    response = {'status': 'ok','result': "Connection established on port ......"}
    return response

def set_params(data):
    for key in data:
        if key == "token":
            continue
        params[key] = data[key]
        ##got the values back nice
    return {'result': 'ok'}

def dir(dirz):
    return True

def pre_fill():
    response = {}
    for key in params:
        response[key] = params[key]
    return response

def getData():
    for key in monitor_vals:
        monitor_vals[key] = random.randrange(100)
    return

def refresh():
    getData()
    response = {'vals': monitor_vals, 'time': time.asctime()}
    return response
