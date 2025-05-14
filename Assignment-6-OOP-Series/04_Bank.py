class Bank:
    bank_name = "Bank of Punjab"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        
b1 = Bank()
b2 = Bank()


print(Bank.bank_name)
Bank.change_bank_name("Bank of Khyber")
print(b1.bank_name)
print(b2.bank_name)



