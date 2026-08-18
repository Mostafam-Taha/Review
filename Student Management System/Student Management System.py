# Student Management System
# Show: Name, ID, Grade
# Show: Ma: Grades
import os
import csv
from datetime import datetime

file_system_management = "Student Management System/student.csv"
fieldnames = ["Name", "ID", "Grade", "Created_at"]

class Student_Management_System:
    def __init__(self):
        pass

    def show_menu(self):
        print("Welcome To User")
        print("1. Add Student")
        print("2. Remove Student")
        # print("3. Update Grade")
        print("3. Displat All Students")
        print("4. Find Student")
        # print("6. Calculate Avarage")
        print("5. Top and Bottom Student")
        # print("6. Sort Students By Avarage")
        print("0. Exit")

    def add_student(self):
        global fieldnames
        # Name
        add_in_name = input("Please enter is name: ")

        # ID
        while True:
            try:
                add_in_ID = int(input(f"Please Enter is ID {add_in_name}: "))
            except ValueError:
                print("Error: Please Enter Is Number not Chracter and Floating number.")
                continue

            # تحقق من التكرار
            if os.path.isfile(file_system_management):
                with open(file_system_management, "r") as check_file:
                    existing_students = csv.DictReader(check_file)
                    duplicate = any(int(row["ID"]) == add_in_ID for row in existing_students)
                if duplicate:
                    print(f"Error: ID {add_in_ID} already exists. Please enter a different ID.")
                    continue
            break

        # Grade
        while True:
            try:
                add_in_grade = float(input(f"Please enter is grade {add_in_name}: "))
                break
            except ValueError:
                print("Error: Please enter number not character.")

        created_at = datetime.now().strftime("%B-%Y-%d %H:%M:%S")
        new_student = {
            "Name": add_in_name,
            "ID": add_in_ID,
            "Grade": add_in_grade,
            "Created_at": created_at
        }

        file_exsits = os.path.isfile(file_system_management)
        with open(file_system_management, "a", newline="") as file_create_student:
            reader = csv.DictWriter(file_create_student, fieldnames=fieldnames)
            if not file_exsits:
                reader.writeheader()
            reader.writerow(new_student)
            
    def remove_student(self):
        global fieldnames
        remove_in_student = input("Please select student and remove: ")

        with open(file_system_management, "r") as f:
            find_student = csv.DictReader(f)
            new_student = []
            for sor in find_student:
                if sor["Name"] != remove_in_student:
                    new_student.append(sor)
        with open(file_system_management, "w", newline="") as create_new_file_after_remove:
            w_create_file = csv.DictWriter(create_new_file_after_remove, fieldnames=fieldnames)
            w_create_file.writeheader()
            w_create_file.writerows(new_student)

    def show_all_student(self):
        with open(file_system_management, "r") as show_d:
            show_d_student = csv.DictReader(show_d)
            for row in show_d_student:
                print(f"  {row["ID"]}: {row["Name"]} | {row["Grade"]} | {row["Created_at"]}")
                print("  -" * 10)

    def find_student(self):
        while True:
            try:
                find_in_ID = int(input("Please enter is ID: "))
                break
            except ValueError:
                print("Error: Please enter is ID, Not Other.")
        with open(file_system_management, "r") as f:
            f_find_student = csv.DictReader(f)
            found = False
            for i in f_find_student:
                if int(i["ID"]) == find_in_ID:
                    print(f"{i["ID"]}: {i["Name"]} - {i["Grade"]} - {i["Created_at"]}")
                    found = True
                    break

            if not found:
                print("Error: No student found with this ID.")

    def sort_students_by_grade(self):
        with open(file_system_management, "r") as s:
            reader = csv.DictReader(s)
            all_students = list(reader)

        sorted_students = sorted(
            all_students,
            key=lambda student: float(student["Grade"]),
            reverse=True
        )

        for student in sorted_students:
            print(f"{student['ID']}: {student['Name']} | {student['Grade']} | {student['Created_at']}")

def main():
    class_sms = Student_Management_System()
    while True:
        class_sms.show_menu()

        while True:
            try:
                user_choose = int(input("Please enter is number: "))
                break
            except ValueError:
                print("Error: Enter is number.")
        if user_choose == 1:
            class_sms.add_student()
        elif user_choose == 2:
            class_sms.remove_student()
        elif user_choose == 3:
            class_sms.show_all_student()
        elif user_choose == 4:
            class_sms.find_student()
        elif user_choose == 5:
            class_sms.sort_students_by_grade()
        else:
            print("Thank you.")
            break

main()
