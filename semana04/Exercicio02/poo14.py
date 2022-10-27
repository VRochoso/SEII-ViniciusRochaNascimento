class Person:
    n_o_p = 0

    def __init__(self,name):
        self.name = name

p1 = Person("vinicius")
p2 = Person("claudia")

print(p1.n_o_p)
print(Person.n_o_p)

Person.n_o_p = 8
print(p2.n_o_p)
Person.n_o_p = 9
print(p1.n_o_p)