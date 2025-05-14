class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    
    @classmethod
    def count_object(cls):
        print(f"The count is {cls.count}")

c1 = Counter()
c2 = Counter()
c3 = Counter()
c4 = Counter()

Counter.count_object()