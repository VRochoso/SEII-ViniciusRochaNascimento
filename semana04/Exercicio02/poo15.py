class Math:
    @staticmethod
    def add5(x):
        return x + 5
    
    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("run")

print(Math.add5(4))
print(Math.add10(4))
Math.pr()