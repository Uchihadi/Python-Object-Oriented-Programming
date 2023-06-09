class Customer:
    def __init__(self, id, name, age, wallet_balance):
        self.id = id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance #Private Attribute

    def set_wallet_balance(self, amount): #Using the setter method, you will be able to invoke private attributes using method
        if amount < 1000 and amount > 0:
            self.__wallet_balance = amount

    def get_wallet_balance(self):
        return self.__wallet_balance

c1=Customer(100, "Gopal", 24, 1000)
c1.set_wallet_balance(120) #Invoking the method with private attributes
print(c1.get_wallet_balance())
