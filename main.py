
class Person:
    def __init__(self, n, s, a):
        self.name = n
        self.surname = s
        self.age = a

    def work(self):
        print("I'm working")

    def info(self):
        print(self.name, self.surname, self.age)

p1 = Person("Umar", "Davlatov", 34)
p2 = Person("Muzaffar", "A", 19)

print(p2.name)
p1.info()

