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
        print("3. Update Grade")
        print("4. Displat All Students")
        print("5. Find Student")
        print("6. Calculate Avarage")
        print("7. Get Letter Grade")
        print("8. Top and Bottom Student")
        print("9. Sort Students By Avarage")
        print("0. Exit")

    def add_student(self):
        global fieldnames
        # Name
        while True:
            try:
                add_in_name = input("Please enter is name: ")
                break
            except ValueError:
                print("Error: Please Enter is character.")
        # ID
        while True:
            try:
                add_in_ID = int(input(f"Please Enter is ID {add_in_name}: "))
                break
            except ValueError:
                print("Error: Please Enter Is Number not Chracter and Floating number.")
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
            w_create_file.writerows(new_student)

    def update_grade():
        update_in_name = input("Please enter name update grade: ")
        while True:
            try:
                update_in_grade = float(input(f"Please enter grade is {update_in_name}: "))
                break
            except ValueError:
                print("Error: Please enter is number not charater.")
        with open(file_system_management, "r") as update_grade_student:
            update_grade_find = csv.DictReader(update_grade_student)
            for i in update_grade_find:
                
Student_Management_System().update_grade()