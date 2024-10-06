# Python modules
# Detailed information about all modules here:
    #https://docs.python.org/3/py-modindex.html

import time
import datetime as dt
import sys, os # system, operation system: modules with info about user
import platform # os platform
from infoModule import getInfo

# posible imports too
from math import sqrt 
print('Square of 25', round(sqrt(25)))

# time
print('Programm works !')
time.sleep(1) # (time: in seconds) program on pause
print('Programm answear after sleep 3s')

# datetime
datetime = dt.datetime.now()
# you can also take from date datetime.now()
dt.datetime.now().time()
dt.datetime.now().date()
dt.datetime.now().weekday()

print('Today is: ', datetime)

# sys
print('path to project: ', sys.path)

# os
print('Device info: ', os.name, platform.system())

# my info module
print('Info', getInfo())