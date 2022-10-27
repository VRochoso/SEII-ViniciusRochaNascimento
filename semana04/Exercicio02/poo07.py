class Dog:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

d = Dog("Joseph")
print(d.get_name())
d2 = Dog("Amorinha")
print(d2.get_name())