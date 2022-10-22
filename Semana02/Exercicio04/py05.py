from optparse import Values
from typing import ItemsView, KeysView


student = {name:'vinicius','age': 25, 'courses': ['math', 'engenharia']}

print(student)
print(student['name'])
print(student['age'])
print(student['coureses'])
#print(student['phone'])
print(student.get('name')
print(student.get('phone')
print(student.get('phone', 'not found')

student['phone'] = 34993218609

student.update({'name': 'joseph', 'age': 4, 'phone':'34993218609'})
print(student)

del student['age']

age = student.pop('age')
print(age)
print(student)

print(student.Keys())
print(student.Values())
print(student.ItemsView())

for key in student:
    print(key)

for key, value in student.ItemsView():
    print(key, value)