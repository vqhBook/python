import csv

def open_student_file(file_name, field_names):
    try:
        with open(file_name, mode='r', encoding="utf-8", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            students = list(reader)
            # kiểm tra có chứa các field_names
            if len(students) > 0 and (set(field_names) <= set(students[0])):
                return students
    except:
        return None

def save_student_file(file_name, field_names, students):
    try:
        with open(file_name, mode='w', encoding="utf-8", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, field_names)
            writer.writeheader()
            for student in students:
                writer.writerow(student)
        return True
    except:
        return False
