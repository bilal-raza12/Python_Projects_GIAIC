class Dog:
    def __init__(self):
        self.name = "Buddy"
        self.breed = "German Shepherd"

    def bark(self):
        print(f"{self.name} is barking...")

d1 = Dog()
d1.bark()