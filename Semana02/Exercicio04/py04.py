from distutils import core


courses = ['history', 'math', 'phisics', 'compsci']
print(courses[])
print(courses[0])
print(courses[3])
print(courses[-1])
##print(courses[4])
print(courses[0:2])
print(courses[:2])
print(courses[2:])

courses.append('art')
print(courses)

courses.insert(0,'science')
print(courses)

courses2 = ['education', 'biology']
courses.insert(0, courses2)
print(courses)
print(courses[0])

courses.extend(courses2)
print(courses)

courses.append(courses2)
print(courses)

courses.remove('math')
print(courses)

courses.pop()
print(courses)

popped = courses.pop()
print(popped)
print(courses)

courses.reverse()
print(courses)

courses.sort()
print(courses)

nums = [1, 4, 5, 6,3,9]
nums.sort()
print(nums)

courses.sort(reverse=True)
nums.sort(reverse=True)
print(courses)
print(nums)

sorted(courses)
print(courses)

sorte_courses = sorted(courses)
print(sorte_courses)

print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index('compsci'))
print(courses.index('art'))

print('art' in courses)
print('math' in courses)

for item in courses:
    print(courses)

for index, item in enumerate(courses):
    print(index, courses)

for index, item in enumerate(courses, start=1):
    print(index, courses)

course_str = ', '.join(courses)
print(course_str)

course_str = ' - '.join(courses)
print(course_str)

newlist = course_str.split(' - ')
print(newlist)

list1 = ['history', 'math', 'phisics', 'compsci']
list2 = list1
print(list1)
print(list2)
list1[0] = 'art'
print(list1)
print(list2)

#list1 = ('history', 'math', 'phisics', 'compsci')
#list2 = list1
#print(list1)
#print(list2)
#list1[0] = 'art'
#print(list1)
#print(list2)

list3 = {'history', 'math', 'phisics', 'compsci'}
print(list3)

list3 = {'history', 'math', 'phisics', 'compsci', 'math'}
print(list3)

print('math' in list3)

list4 = {'history', 'math', 'phisics', 'compsci'}
list5 = {'history', 'math', 'art', 'design'}
print(list4.intersection(list5))
print(list4.difference(list5))
print(list4.union(list5))

emptylist = []
emptylist = list[]

emptytuple = ()
emptytuple = tuple()

#emptyset = {}
emptyset = set()
