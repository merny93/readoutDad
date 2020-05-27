"""
Application stub
"""
import sys

def initialize():
    #will run everytime any page loads

    print('Hello world!', file=sys.stderr)

    return True


def do_stuff():
    # do whatever you need to do
    response = "This is response from Python backend"
    return response

def serial_connection():
    print("hello", file=sys.stderr)
    return True

def set_params(stuff):
    return True

def dir(dirz):
    return True