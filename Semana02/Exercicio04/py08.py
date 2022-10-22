from xml.dom import NotFoundErr


def hello_func():
    pass

print(hello_func)
print(hello_func())

def hello_func():
    print('hello function.')
    
hello_func()

def hello_func():
    return 'hello function.'

print(hello_func())

print(len('test'))

print(hello_func().upper())

def hello_func(greeting):
    return '{} Function.'.format(greeting)

print(hello_func('hi'))

def hello_func(greeting, name='you'):
    return '{}, {}'.format(greeting, name)
print(hello_func('hi',name='vinicius'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('math','art', name='jhon', age=28)

courses = ['math','art']
info = {'name': 'jhon', 'age': 28}
student_info(courses, info)
student_info(*courses, **info)

month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 !=  or year % 400 == 0)

def daysinmonth(year,month):
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]

print(is_leap(2017))
print(is_leap(2020))
print(daysinmonth(2017, 2))