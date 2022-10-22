from msilib.schema import Condition


language = 'python'

if language == 'python':
    print('conditional was true')

## comparaçoes
## igual 3==2
## diferente 3 != 2
## maior que 3>2
## menor que 2<3
## maior ou igual 3 >= 2
## menor ou igual 2 <= 3
## objeto de identidadae is
## and
## or
## not

if language == 'python':
    print('lenguage is python')
else:
    print('no match')


language2 = 'java'
if language2 == 'python':
    print('lenguage is python')
else:
    print('no match')


language2 = 'java'
if language2 == 'python':
    print('lenguage is python')
elif language2 == 'java':
    print('language is java')
else:
    print('no match')

language3 = 'java'
if language3 == 'python':
    print('lenguage is python')
elif language3 == 'java':
    print('language is java')
elif language3 == 'javascript':
    print('language is javascript')
else:
    print('no match')

user = 'admin'
logged_in = False
if user == 'admin' and logged_in:
    print('admin page')
else:
    print('bad creds')

if user == 'admin' or logged_in:
    print('admin page')
else:
    print('bad creds')

if not logged_in:
    print('please log in')
else:
    print('welcome')

a =[1,2,3]
b =[1,2,3]
print(a == b)
print(a is b)
print(id(a))
print(id(b))

b = a
print(id(a))
print(id(b))
print(a == b)
print(a is b)
print(id(a) == id(b))

condition = False
if condition:
    print('evaluated to true')
else:
    print('evaluated to false')

condition = None
if condition:
    print('evaluated to true')
else:
    print('evaluated to false')

condition = 0
if condition:
    print('evaluated to true')
else:
    print('evaluated to false')

condition = 10
if condition:
    print('evaluated to true')
else:
    print('evaluated to false')

condition = []
if condition:
    print('evaluated to true')
else:
    print('evaluated to false')

condition = {}
if condition:
    print('evaluated to true')
else:
    print('evaluated to false')

condition = ''
if condition:
    print('evaluated to true')
else:
    print('evaluated to false')

condition = 'test'
if condition:
    print('evaluated to true')
else:
    print('evaluated to false')