# Password Manager
# 1. انشاء حساب خاص بالمستخدم, يكون (اسم المستخدم, كلمة المرور)
# 2. طلب من المستخدم ادخال كلمة المرور فى كل مره يطلب يريد عرض كلمة مرور ما
# 3. فتح نفاذة القوائم للختيار
# 4. اذا كانت هناك اي بيانات خطأ لا يتم الارسال إللى قائمة الاختيارات الخاصة بالبرنامج ابدًا
import os
import csv
import random
from datetime import datetime

file_system_management = "Project Password Manager/password.csv"

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

def show_menu_account():
    print("Welcome To User")
    print("1. Sign_UP")
    print("2. Login")
    print("3. Switch Accounts")

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
        else:
            print("Thank you!")
            break

log_main()