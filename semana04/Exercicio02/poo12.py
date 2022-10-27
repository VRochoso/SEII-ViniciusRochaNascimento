class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and i am {self.age} years old")
    
    def speak(self):
        print("hi human")

class Cat(Pet):
    def speak(self):
        print("Meow")

class Dog(Pet):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("Bark")


p = Pet("joseph", 4)
p.show()
p.speak()
c = Cat("Tobias", 2)
c.show()
c.speak()
a = Dog("amorinha", 2)
a.show()
a.speak()

