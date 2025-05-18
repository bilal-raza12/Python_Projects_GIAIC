class Order(object):
    def __init__(self , order_id , order_status ):
        self.order_id = order_id
        self.order_status = "Recieved"
    
class Order_Process(Order):
    def __init__(self , order_id , payment , order_status):
        super().__init__(order_id , order_status)
        self.payment = payment
print(Order_Process.mro())
o1 = Order_Process(1 , 1000 , "Recieved")
        
        
        
