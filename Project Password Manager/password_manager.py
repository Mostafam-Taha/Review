# Password Manager
import os
import csv
import random
from datetime import datetime

file_system_management = "Project Password Manager/data_user.csv"
file_system_user_acc = "Project Password Manager/password.csv"

class Login_Password_Manager:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def sign_in(self):
        while True:
            in_username = input("Enter your username: ")

            if os.path.isfile(file_system_management):
                with open(file_system_management, "r") as check_file:
                    find_username_check = csv.DictReader(check_file)
                    duplicate = any(row["Username"] == in_username for row in find_username_check)
                if duplicate:
                    print(f"Error: Username {in_username} already exists. Please enter a different Username.")
                    continue
            break
        in_password = input("Enter your password: ")

        in_user_ID = random.randint(1000000,1000000000)

        created_at = datetime.now().strftime("%B-%Y-%d %H:%M:%S")
        new_sign_in_user_manager = {
            "ID_User": in_user_ID,
            "Username": in_username,
            "Password": in_password,
            "Created_at": created_at
        }

        fieldnames = ["ID_User", "Username", "Password", "Created_at"]
        file_exist = os.path.isfile(file_system_management)
        with open(file_system_management, "a", newline="") as file_as_password_user_manager:
            file_user = csv.DictWriter(file_as_password_user_manager, fieldnames=fieldnames)
            if not file_exist:
                file_user.writeheader()
            file_user.writerow(new_sign_in_user_manager)

    def login(self):
        with open(file_system_management, "r") as file_reader:
            reader = csv.DictReader(file_reader)
            lo_username = input("Enter your username: ")
            lo_password = input("Please enter your password: ")

            found = False
            for i in reader:
                if lo_username == i["Username"] and lo_password == i["Password"]:
                    print("done", lo_username, lo_password) # تعديل
                    found = True
                    break

            if not found:
                print("Error: Incorrent.")

class Password_Manager:
    def __init__(self):
        pass

    def add_new_password(self):
        application_password = input("Please enter your application: ")
        choose_app = input("Do you want to create a random password Y/n: ")
        URL_application = input(f"Please enter your URL {application_password}: ")

        application_random = None
        in_user_password_m = None
        while True:
            if choose_app == "Y":
                application_random = random.randint(10000000, 100000000000)
                in_random_ag = input(f"Dono: Create Password this: {application_random} Y/n: ")
                if in_random_ag == "Y":
                    application_random = random.randint(10000000, 100000000000)
                    in_random_ag_loop = input(f"Dono: Create Password this: {application_random} Y/n: ")
                    if in_random_ag_loop == "Y":
                        continue
                    else:
                        break
                else:
                    break
            else:
                in_user_password_m = input("Please Enter you password: ")
                break

        created_at = datetime.now().strftime("%B-%Y-%d %H:%M:%S")
        new_add_passwrod = {
            "Application": application_password,
            "Password": in_user_password_m if not application_random else None,
            "Random Password": application_random if application_random else None,
            "Created_at": created_at
        }

        fieldnames = ["Application", "Password", "Random Password", "Created_at"]

        file_exist = os.path.isfile(file_system_user_acc)
        with open(file_system_user_acc, "a", newline="") as file_user_acc:
            file_re = csv.DictWriter(file_user_acc, fieldnames=fieldnames)
            if not file_exist:
                file_re.writeheader()
            file_re.writerow(new_add_passwrod)

    def show_all_password(self):
        with open(file_system_user_acc, "r") as file_reader:
            reader = csv.DictReader(file_reader)
            print(f"{'Application':<20}{'Password':<15}{'Random Password':<20}{'Created_at':<25}")
            for show_all  in reader:
                print(f"{show_all['Application']:<20}: {show_all['Password']:<15} | {show_all['Random Password']:<20} | {show_all['Created_at']:<25}")

    def search_to_password(self):

        with open(file_system_user_acc, "r") as file_reader:
            reader = csv.DictReader(file_reader)

            found = False
            search_application = input("Enter your application: ")
            for search in reader:
                if search_application in search["Application"]:
                    print(f"{search['Application']:<10}{search['Password']:<8}{search['Random Password']:<10}{search['Created_at']:<10}")
                    found = True
                    break

            if not found:
                print("Application not found.")


def show_menu_account():
    print("Welcome To User")
    print("1. Sign_UP")
    print("2. Login")
    print("3. Switch Accounts")
    print("4. Login_account_manager (Bita)")

def show_menu():
    user = Login_Password_Manager("Mostafamtaha", 1234)
    print(f"==== Welcome To {user.username}")
    print("1. Add New Password")
    print("2. Show All Password")
    print("3. Search To Password")

def main():
    user_manager = Login_Password_Manager("Mostafamtaha", 1234)
    user = Password_Manager()

    while True:
        show_menu()
        choose_value = int(input("Please enter you option: "))

        if choose_value == 1:
            user.add_new_password()
        elif choose_value == 2:
            user.show_all_password()
        elif choose_value == 3:
            user.search_to_password()
        else:
            print(f"Thank You {user_manager.username}")
            break

def log_main():
    user_manager = Login_Password_Manager("Mostafamtaha", 1234)

    while True:
        while True:
            show_menu_account()

            try:
                user_select = int(input("Pealse select an option number: "))
                break
            except ValueError:
                print("Error: Option number.")
                continue

        if user_select == 1:
            user_manager.sign_in()
        elif user_select == 2:
            user_manager.login()
        elif user_select == 3:
            pass
        elif user_select == 4:
            main()
        else:
            print("Thank you!")
            break

log_main()
