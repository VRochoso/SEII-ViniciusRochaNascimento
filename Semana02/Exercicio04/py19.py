li = [9,1,8,2,7,3,6,4,5]
sli = sorted(li)
print('sorted variable:\t', sli)
li.sort()
print('original variable:\t', li)

sli = sorted(li, reverse=True)
li.sort(reverse=True)

tup = (9,1,8,2,7,3,6,4,5)
stup = sorted(tup)
print('Tuple\t', stup)

di = {'name': 'vini', 'job': 'studer', 'age': None, 'os': 'ubuntu'}
sdi = sorted(di)
print('Dict\t', sdi)

li = [-6,-5,-4,1,2,3]
sli = sorted(li, key=abs)
print(sli)

class Employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

from operator import attrgetter

e1 = Employee('carl', 37, 7000)
e2 = Employee('sarah', 29, 2000)
e3 = Employee('john', 43, 3000)

employees = [e1,e2,e3]
def esort(emp):
    return emp.age

def esort(emp):
    return emp.salary

def esort(emp):
    return emp.name 

semployees = sorted(employess, key=esort, reverse=True)
semployees = sorted(employess, key=lambda e: e.name)
semployees = sorted(employess, key=attrgetter('age'))
print(semployees)