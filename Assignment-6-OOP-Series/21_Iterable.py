from collections.abc import Iterable,Iterator


class CountDown(Iterable):
    def __init__(self , start):
        self.current = start
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            current = self.current
            self.current -= 1
            return current
    
countdown = CountDown(5)
for i in countdown:
    print(i)


