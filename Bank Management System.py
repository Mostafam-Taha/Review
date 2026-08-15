#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==================================================
   نظام إدارة بنك متكامل (Bank Management System)
==================================================
مشروع بايثون كامل يحاكي نظام بنك بسيط يعمل عبر الطرفية (Console).

المميزات:
- سحب أموال (مع التحقق من الرصيد)
- تحويل أموال بين الحسابات
- عرض الرصيد
- عرض كشف الحساب (سجل العمليات)
- لوحة تحكم للمدير (Admin): عرض كل الحسابات، إجمالي أموال البنك، حذف حساب، تجميد/تفعيل حساب
- التحقق من صحة المدخلات ومعالجة الأخطاء

بيانات المدير الافتراضية:
    اسم المستخدم: admin
    كلمة المرور: admin123
(يمكن تغييرها من داخل الكود في متغير ADMIN_USERNAME و ADMIN_PASSWORD)
"""

class Bank_Management_System():
    balance_create_account = 0
    def __init__(self, username_account, kaumy, pin):
        self.username_account = username_account
        self.create_kaumy = kaumy
        self.create_pin = pin
        self.back_up_accounts = {}

    def new_account_s(self):
        if self.create_kaumy in self.back_up_accounts:
            print(f"Error: this is account old, not new {self.username_account}")
        else:
            self.back_up_accounts[self.create_kaumy] = self.username_account, self.create_pin, Bank_Management_System.balance_create_account

    # == input ==
    def deposit(self, amount):
        if amount > 0:
            Bank_Management_System.balance_create_account += amount

    # == input ==
    def withdrow(self, amount):
        if amount <= Bank_Management_System.balance_create_account:
            if amount > 0:
                Bank_Management_System.balance_create_account -= amount
                print(f"Done: Withdrow {amount} EGP, Balance New: {Bank_Management_System.balance_create_account} EGP")
            else:
                print(f"Error: Amount: {amount} EGP, <= Zoro")

        else:
            print(f"Error: amount greate then {Bank_Management_System.balance_create_account}")

    def __str__(self):
        return f"Done: Name: {self.username_account}\nNumber_human: {self.create_kaumy}\nPIN: {self.create_pin}\nBalance: {Bank_Management_System.balance_create_account}"
    
def sigh_up():
    username = input("Enter is Username: ")
    kaumy = int(input("Enter is number human: "))
    PIN_account = int(input("Enter is PIN Account: "))
    my_new_account = Bank_Management_System(username, kaumy, PIN_account)
    my_new_account.new_account_s()
    print(my_new_account.__str__())

def ATM_deposit_and_withdrow():
    my_test = Bank_Management_System("mostafa", 4654, 213)
    my_test.deposit(1200)
    my_test.withdrow(11010)
    print(my_test.__str__())
    my_test.new_account_s()
    print(my_test.back_up_accounts)

ATM_deposit_and_withdrow()
