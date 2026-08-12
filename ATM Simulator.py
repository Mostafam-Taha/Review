# ATM Simulator

balance = 1000
PIN = 1234
number_of_att = 3
attemes = 0

print("====Welcome to ATM====")

while attemes != number_of_att:
    user_pin = int(input("Please Enter PIN"))

    if user_pin == PIN:
        print("Correct")
        break
    else:
        print("Incorrect")
        if len(str(user_pin)) != 4:
            print("Ammm, Tihs is 4 chracters")
            continue

        attemes += 1
        if attemes == number_of_att:
            print("Black program")
            break

def show_menu():
    print("\n==== Menu ====")
    print("1. Show balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("0. Exit")

def show_balance():
    print(f"Tihs is balance: {balance} EGP")

def deposit():
    global balance
    balance_deposit = int(input("Please enter you deposit: "))

    if balance_deposit > 0:
        balance = balance_deposit + balance
        print(f"Done deposit {balance_deposit} EGP, balance new {balance} EGP")
        return balance
    else:
        print("Block")

def withdraw():
    global balance
    balance_withdraw = int(input("Please enter you withdraw balance: "))

    if balance_withdraw < 0 or balance_withdraw > balance:
        print("Failed")
    else:
        balance = balance - balance_withdraw
        print(f"Done Withdraw {balance_withdraw} EGP, balance new {balance} EGP")
        return balance

def main():
    while True:
        show_menu()
        user_Experins = input("Please Enter is number: ")

        if user_Experins == "1":
            show_balance()
        elif user_Experins == "2":
            deposit()
        elif user_Experins == "3":
            withdraw()
        else:
            print("Thank you.")
            break

# Accssis is Password

if  user_pin == PIN:
    main()

else:
    print("Sorry passwrod is incorrect")