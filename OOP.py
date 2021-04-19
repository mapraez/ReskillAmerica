class Budget:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def check_balance(self):
        print("%s category current Balance is: $%d" % (self.category, self.amount))

    def deposit(self, amount):
        print("-" * 10)
        print("Depositing $%d" % amount)
        self.amount += amount
        return self.check_balance()

    def withdraw(self, amount):
        print("-" * 10)
        print("Withdrawing $%d" % amount)
        self.amount += amount
        return self.check_balance()

    def transfer(self, other, amount):
        print("-" * 10)
        print("Checking balances:")
        self.check_balance()
        other.check_balance()
        print("-" * 5)
        print("Transferring Funds")
        if self.amount >= amount:
            self.amount -= amount
            other.amount += amount
            print("Funds transferred")
            self.check_balance()
            other.check_balance()
        else:
            print("Not enough funds")




obj = Budget('Clothing', 1000)
obj_1 = Budget('Food', 1000)
obj_2 = Budget('Entertainment', 1000)


print("-" * 20)
print("-" * 20)
print(obj.category)
print(obj.amount)
obj.deposit(5)
obj.withdraw(10)
obj.transfer(obj_1, 50)

print("-" * 20)
print("-" * 20)
print(obj_1.category)
print(obj_1.amount)
obj_1.deposit(5)
obj_1.withdraw(10)
obj_1.transfer(obj_2, 50)

print("-" * 20)
print("-" * 20)
print(obj_2.category)
print(obj_2.amount)
obj_2.deposit(5)
obj_2.withdraw(10)
obj_2.transfer(obj, 50)