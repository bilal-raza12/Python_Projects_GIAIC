class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()
    
    def start(self):
        self.engine.start()
        
c1 = Car()
c1.start()