def add_greeting(cls):
    def greet(self):
        print("Hello from the decorator!")
    
    cls.greet = greet

    return cls
    
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Bilal")
p1.greet()