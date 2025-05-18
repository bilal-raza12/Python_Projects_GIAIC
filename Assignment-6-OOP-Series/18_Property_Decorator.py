class Product:
    def __init__(self , price):
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self , new_price):
        if new_price > 0 and type(new_price) == int:
            self._price = new_price

    @price.deleter
    def price(self):
        del self._price
        print("Price deleted")

p1 = Product(100)
print(p1.price)
p1.price = 200
print(p1.price)
del p1.price
