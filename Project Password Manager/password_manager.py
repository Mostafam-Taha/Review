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
        in_username = input("Enter your username: ")
        
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
            
user = Login_Password_Manager("Mostafa", 1234)
user.login()
