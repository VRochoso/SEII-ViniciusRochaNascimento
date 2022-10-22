from operator import index
import my_module
courses = ['history', 'math', 'phisics', 'compsci']
index = my_module.find_index(courses, 'math')
print(index)


import my_module as mm
courses = ['history', 'math', 'phisics', 'compsci']
index = mm.find_index(courses, 'math')
print(index)

from my_module import find_index
courses = ['history', 'math', 'phisics', 'compsci']
index = find_index(courses, 'math')
print(index)

from my_module import find_index, test
courses = ['history', 'math', 'phisics', 'compsci']
index = find_index(courses, 'math')
print(index)
print(test)

from my_module import find_index as fi, test
courses = ['history', 'math', 'phisics', 'compsci']
index = fi(courses, 'math')
print(index)
print(test)

from my_module import *
courses = ['history', 'math', 'phisics', 'compsci']
index = find_index(courses, 'math')
print(index)
print(test)

from my_module import find_index, test
import sys
courses = ['history', 'math', 'phisics', 'compsci']
index = find_index(courses, 'math')
print(sys.path)

import sys
sys.path.append('local do arquivo')
from my_module import find_index, test
courses = ['history', 'math', 'phisics', 'compsci']
index = find_index(courses, 'math')
print(sys.path)

import random
courses = ['history', 'math', 'phisics', 'compsci']
random_course = random.choice(courses)
print(random_course)

import math
courses = ['history', 'math', 'phisics', 'compsci']
rads = math.radians(90)
print(math.sin(rads))

import datetime
import calendar
courses = ['history', 'math', 'phisics', 'compsci']
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

import os
courses = ['history', 'math', 'phisics', 'compsci']
print(os.getcwd())
print(os.__file__)