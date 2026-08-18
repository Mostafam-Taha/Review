# 🎓 Student Management System

A Python CLI application designed to manage student records efficiently using **Object-Oriented Programming (OOP)** and persistent storage with **CSV files**.

---

## 📌 Features

- **Add Student:** Register a new student with Name, unique ID, and Grade. Includes automatic duplicate ID check and input validation.
- **Remove Student:** Safely remove a student record by name from the file.
- **Display All Students:** View a formatted list of all registered students along with their creation timestamp.
- **Find Student:** Search for a specific student record instantly by entering their ID.
- **Sort Students:** Rank students based on their grades in descending order (Highest to Lowest).
- **Data Persistence:** Automatically creates and updates `student.csv` to ensure data is never lost between sessions.

---

## 🛠️ Tech Stack & Concepts Applied

- **Language:** Python 3
- **Paradigm:** Object-Oriented Programming (OOP)
- **Data Storage:** Flat-file database using standard `csv` module
- **Validation:** Exception handling with `try-except` blocks to prevent crashes on invalid user input
- **Modules Used:** `os`, `csv`, `datetime`

---

## 📁 Folder Structure

```text
Student Management System/
├── Student Management System.py    # Main program script
└── student.csv                     # Auto-generated CSV file for data persistence
