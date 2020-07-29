"""
Application stub
"""
import sys



params = {}
default_params = {
    'name':10,
    'value': 20,
    'stuff': 30
}


def initialize():
    #will run everytime any page loads
    pass
    return True



def serial_connection():
    response = "Connection established on port ......"
    return response

def set_params(data):
    for key in data:
        if key == "token":
            continue
        params[key] = data[key]
        ##got the values back nice
    return True

def dir(dirz):
    return True

def pre_fill(data):
    response = {}
    for key in data:
        if key == "token":
            continue
        field = data[key]
        print(field, file=sys.stderr)
        if field not in params.keys():
            try:
                response[field] = default_params[field]
            except KeyError:
                response[field] = "no preset"
        else:
            response[field] = params[field]
    return response