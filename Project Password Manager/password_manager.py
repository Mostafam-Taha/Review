# Password Manager
# 1. انشاء حساب خاص بالمستخدم, يكون (اسم المستخدم, كلمة المرور)
# 2. طلب من المستخدم ادخال كلمة المرور فى كل مره يطلب يريد عرض كلمة مرور ما
# 3. فتح نفاذة القوائم للختيار
# 4. اذا كانت هناك اي بيانات خطأ لا يتم الارسال إللى قائمة الاختيارات الخاصة بالبرنامج ابدًا
import random

class Login_Password_Manager:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def sign_in(self):
        in_username = input("Enter your username: ")
        
        in_password = input("Enter your password: ")

        In_user_ID = random.randint(1000000,100000000)
        print(In_user_ID)
        # هكمل الكود بعد مصحى من النوم 😴 ان شاء الله

user = Login_Password_Manager("Mostafa", 1234)
user.sign_in()