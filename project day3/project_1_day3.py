attendance = {}

def add_student():
    name = input("Enter student name: ")

    if name in attendance:
        print("Student already exists.")
    else:
        attendance[name] = []
        print("Student added successfully!")


def mark_attendance():
    name = input("Enter student name: ")

    if name in attendance:
        status = input("Enter attendance (P/A): ").upper()

        if status == "P" or status == "A":
            attendance[name].append(status)
            print("Attendance marked successfully!")
        else:
            print("Invalid attendance.")
    else:
        print("Student not found.")


def view_attendance():
    if len(attendance) == 0:
        print("No students available.")
    else:
        for student, record in attendance.items():
            print(student, ":", record)

def attendance_percentage():
    name = input("Enter student name: ")

    if name in attendance:

        total = len(attendance[name])

        if total == 0:
            print("No attendance recorded.")
        else:
            present = attendance[name].count("P")
            percentage = (present / total) * 100

            print("Attendance Percentage =", percentage, "%")
    else:
        print("Student not found.")


while True:

    print("\n----- Attendance Management System -----")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Attendance Percentage")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        mark_attendance()

    elif choice == "3":
        view_attendance()

    elif choice == "4":
        attendance_percentage()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")