class Car:
    def __init__(self , brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} is started...")

c1 = Car("BMW")

c1.start()