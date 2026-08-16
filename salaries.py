import csv
def add_new_salaries(row):
    salary = float(row["salary"]) * 1.1
    row["new_salary"] = round(salary, 2)
    return row

with open("salaries.csv", "r") as old_file, open("new_salaries.csv", "w") as new_file:
    reader = csv.DictReader(old_file)
    column = reader.fieldnames + ["new_salary"]
    write = csv.DictWriter(new_file, column)
    write.writeheader()
    for i in reader:
        write.writerow(i)