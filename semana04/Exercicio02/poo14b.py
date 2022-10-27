class Person:
    n_o_p = 0

    def __init__(self,name):
        self.name = name
        Person.n_o_p += 1

p1 = Person("vinicius")
print(Person.n_o_p)
p2 = Person("claudia")
print(Person.n_o_p)
