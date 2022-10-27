class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and i am {self.age} years old")
    
    def speak(self):
        print("hi human")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color
    
    def speak(self):
        print("Meow")
    
    def show(self):
        print(f"i am {self.name} and i am {self.age} years old and i am {self.color}")

class Dog(Pet):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("joseph", 4)
p.show()
p.speak()
c = Cat("Tobias", 2, "amarelo")
c.show()
c.speak()
a = Dog("amorinha", 2)
a.show()
a.speak()
f = Fish("beta", 99)
f.show()
f.speak()

