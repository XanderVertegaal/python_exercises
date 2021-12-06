# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

import this
from time import sleep
from math import sin
from datetime import datetime
from sys import platform as myplatform
from greet import supergreeting

def wait(seconds: int):
    sleep(seconds)
    return

def my_sin(number: float):
    return sin(number)

def iso_now():
    return datetime.now().isoformat(timespec='minutes')

def platform():
    return myplatform

def supergreeting_wrapper(name):
    return supergreeting(name)

print(supergreeting_wrapper('Henry'))