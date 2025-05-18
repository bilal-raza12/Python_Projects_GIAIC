class A:
    def show(self):
        print("Hello from A")
class B(A):
    def show(self):
        print("Hello from B")
class C(A):
    def show(self):
        print("Hello from C")

class D(B, C):
    pass

d = D()
print(D.mro())
d.show()