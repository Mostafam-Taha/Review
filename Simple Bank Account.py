class BankAccount():
    def __init__(self, owner, balance):
        self.owner_name = owner
        self.balance = balance
        self.histore = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.histore.append(amount)
        else:
            print(f"Error: your balance {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: المبلغ لازم يكون أكبر من صفر")
        elif amount > self.balance:
            print("Error: الرصيد غير كافٍ")
        else:
            self.balance -= amount
            self.histore.append(amount * -1)

    def __str__(self):
        return (f"Name: {self.owner_name}, balance: {self.balance} EGP.")