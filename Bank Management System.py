class Bank_Management_System():
    balance_create_account = 0
    def __init__(self, username_account, kaumy, pin):
        self.username_account = username_account
        self.create_kaumy = kaumy
        self.create_pin = pin
        self.back_up_accounts = {}
        self.history_account = []

    def new_account_s(self):
        if self.create_kaumy in self.back_up_accounts:
            print(f"Error: this is account old, not new {self.username_account}")
        else:
            self.back_up_accounts[self.create_kaumy] = self.username_account, self.create_pin, Bank_Management_System.balance_create_account

    def deposit(self, amount):
        if amount > 0:
            Bank_Management_System.balance_create_account += amount
            self.history_account.append(amount)
            print(f"Done: Added {amount} EGP to your account, Balance New {Bank_Management_System.balance_create_account}")

    def withdrow(self, amount):
        if amount <= Bank_Management_System.balance_create_account:
            if amount > 0:
                Bank_Management_System.balance_create_account -= amount
                self.history_account.append(amount * -1)
                print(f"Done: Withdrow {amount} EGP, Balance New: {Bank_Management_System.balance_create_account} EGP")
            else:
                print(f"Error: Amount: {amount} EGP, <= Zoro")

        else:
            print(f"Error: amount greate then {Bank_Management_System.balance_create_account}")

    def delete_account(self, input_pin):
        if self.create_pin == input_pin:
            self.back_up_accounts.clear()
            print("Done: remove data saccss.")
        else:
            print("Error: PIN Incorrect.")

    def history(self):
        print(f"{self.history_account}")

    def show_balance(self):
        print(f"Your current balance is {Bank_Management_System.balance_create_account}")

    def __str__(self):
        return f"Done: Name: {self.username_account}\nNumber_human: {self.create_kaumy}\nPIN: {self.create_pin}\nBalance: {Bank_Management_System.balance_create_account}"

def sigh_up(name_c, kaumy_c, PIN_c):
    my_new_account = Bank_Management_System(name_c, kaumy_c, PIN_c)
    my_new_account.new_account_s()
    print(my_new_account.__str__())

def show_menu():
    print("==== Welcome to ====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdrow")
    print("4. Show Balance")
    print("5. Account Statement")
    print("6. Delete Account")
    print("0. Exit")

def main():
    while True:
        show_menu()
        owner_name = ""
        owner_kaumy = 0
        owner_PIN = 0

        user_menu = input("Please Enter you menu: ")
        if user_menu == "1":
            username = input("Enter is Username: ")
            x = username
            kaumy = int(input("Enter is number human: "))
            y = kaumy
            PIN_account = int(input("Enter is PIN Account: "))
            z = PIN_account
            sigh_up(username, kaumy, PIN_account)
        elif user_menu == "2":
            amount_acc_deposit = int(input("Please enter is amount: "))
            my_account_deposit = Bank_Management_System(owner_name, owner_kaumy, owner_PIN)
            my_account_deposit.new_account_s 
            my_account_deposit.deposit(amount_acc_deposit)
        elif user_menu == "3":
            amount_acc_with_draw = int(input("Please enter is amount: "))
            my_account_withdrow = Bank_Management_System(owner_name, owner_kaumy, owner_PIN)
            my_account_withdrow.new_account_s()
            my_account_withdrow.withdrow(amount_acc_with_draw)
        elif user_menu == "4":
            my_account_show_balance = Bank_Management_System(owner_name, owner_kaumy, owner_PIN)
            my_account_show_balance.new_account_s()
            my_account_show_balance.show_balance()
        elif user_menu == "5":
            my_account_history = Bank_Management_System(owner_name, owner_kaumy, owner_PIN)
            my_account_history.new_account_s()
            my_account_history.history()
        elif user_menu == "6":
            pin_acc = int(input("Enter you pin: "))
            Bank_Management_System(owner_name, owner_kaumy, owner_PIN).delete_account(pin_acc)
        else:
            print(f"Exit: Thank you {owner_name}!")
            break

main()
