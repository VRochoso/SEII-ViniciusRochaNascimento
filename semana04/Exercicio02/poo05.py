class Dog:
    def add_1(self,x):
        return x+1

    def meow(self):
        return "meow"
        print("meow")

    def bark(self):
        print("bark")

d = Dog()
print(type(d))
d.meow()
d.bark()
print(d.add_1(5))