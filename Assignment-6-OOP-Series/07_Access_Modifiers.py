class Employee:
    def __init__(self , name , salary , ssn):
        self.name = name #public
        self._salary = salary #protected
        self.__ssn = ssn   #private

emp1 = Employee("Ali" , 1000 , "1234")
print(emp1.name) # public
print(emp1._salary) # protected
#print(emp1.__ssn) # private
    
        