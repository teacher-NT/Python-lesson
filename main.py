class A:
    def __init__(self, n):
        self.name = n

    def salom(self, ism):
        print(f"Salom {ism}")

class B:
    def hayr(self, n):
        print(f"Hayr {n}")

class C(A, B):
    pass

c1 = C(1)
c1.salom("Islom")
c1.hayr("Xojiakbar")

