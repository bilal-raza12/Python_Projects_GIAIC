class Person:
    def __init__(self , name):
        self.name = name
        print(f"Name: {self.name}")

class Teacher(Person):
    def __init__(self , subject , name):
        super().__init__(name)
        self.subject = subject
        print(f"Subject : {self.subject}")



t1 = Teacher("Math" , "Ahmed")
