class Person:
    n_o_p = 0

    def __init__(self,name):
        self.name = name
        Person.add_person()
    @classmethod
    def n_o_p_(cls):
        return cls.n_o_p
    
    @classmethod
    def add_person(cls):
        cls.n_o_p += 1

p1 = Person("vinicius")
p2 = Person("claudia")
print(Person.n_o_p_())
