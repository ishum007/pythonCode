students = []

# ----------------------------
# Calculate Grade
# ----------------------------
def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


# ----------------------------
# Add Student
# ----------------------------
def add_student():
    print("\n----- Add Student -----")

    name = input("Enter Student Name: ")
    roll_number = input("Enter Roll Number: ")

    english_marks = float(input("Enter English Marks: "))
    math_marks = float(input("Enter Math Marks: "))
    science_marks = float(input("Enter Science Marks: "))
    computer_marks = float(input("Enter Computer Marks: "))
    hindi_marks = float(input("Enter Hindi Marks: "))

    total_marks = (
        english_marks
        + math_marks
        + science_marks
        + computer_marks
        + hindi_marks
    )

    percentage = (total_marks / 500) * 100
    grade = calculate_grade(percentage)

    if percentage >= 40:
        result = "Pass"
    else:
        result = "Fail"

    student = {
        "name": name,
        "roll_number": roll_number,
        "english_marks": english_marks,
        "math_marks": math_marks,
        "science_marks": science_marks,
        "computer_marks": computer_marks,
        "hindi_marks": hindi_marks,
        "total_marks": total_marks,
        "percentage": percentage,
        "grade": grade,
        "result": result,
    }

    students.append(student)

    print("\nStudent Added Successfully!")


# ----------------------------
# Display Students
# ----------------------------
def display_students():
    if len(students) == 0:
        print("\nNo Students Found.")
        return

    print("\n===== Student Records =====")

    for student in students:
        print("----------------------------")
        print("Name:", student["name"])
        print("Roll Number:", student["roll_number"])
        print("English:", student["english_marks"])
        print("Math:", student["math_marks"])
        print("Science:", student["science_marks"])
        print("Computer:", student["computer_marks"])
        print("Hindi:", student["hindi_marks"])
        print("Total Marks:", student["total_marks"])
        print("Percentage:", round(student["percentage"], 2), "%")
        print("Grade:", student["grade"])
        print("Result:", student["result"])


# ----------------------------
# Search Student
# ----------------------------
def search_student():
    roll_number = input("Enter Roll Number to Search: ")

    for student in students:
        if student["roll_number"] == roll_number:
            print("\nStudent Found")
            print("----------------------------")
            print("Name:", student["name"])
            print("Roll Number:", student["roll_number"])
            print("English:", student["english_marks"])
            print("Math:", student["math_marks"])
            print("Science:", student["science_marks"])
            print("Computer:", student["computer_marks"])
            print("Hindi:", student["hindi_marks"])
            print("Total Marks:", student["total_marks"])
            print("Percentage:", round(student["percentage"], 2), "%")
            print("Grade:", student["grade"])
            print("Result:", student["result"])
            return

    print("\nStudent Not Found.")


# ----------------------------
# Delete Student
# ----------------------------
def delete_student():
    roll_number = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["roll_number"] == roll_number:
            students.remove(student)
            print("\nStudent Deleted Successfully!")
            return

    print("\nStudent Not Found.")


# ----------------------------
# Update Student
# ----------------------------
def update_student():
    roll_number = input("Enter Roll Number to Update: ")

    for student in students:
        if student["roll_number"] == roll_number:

            student["name"] = input("Enter New Name: ")

            student["english_marks"] = float(input("Enter New English Marks: "))
            student["math_marks"] = float(input("Enter New Math Marks: "))
            student["science_marks"] = float(input("Enter New Science Marks: "))
            student["computer_marks"] = float(input("Enter New Computer Marks: "))
            student["hindi_marks"] = float(input("Enter New Hindi Marks: "))

            total_marks = (
                student["english_marks"]
                + student["math_marks"]
                + student["science_marks"]
                + student["computer_marks"]
                + student["hindi_marks"]
            )

            percentage = (total_marks / 500) * 100

            student["total_marks"] = total_marks
            student["percentage"] = percentage
            student["grade"] = calculate_grade(percentage)

            if percentage >= 40:
                student["result"] = "Pass"
            else:
                student["result"] = "Fail"

            print("\nStudent Updated Successfully!")
            return

    print("\nStudent Not Found.")


# ----------------------------
# Class Topper
# ----------------------------
def class_topper():
    if len(students) == 0:
        print("\nNo Students Found.")
        return

    topper = students[0]

    for student in students:
        if student["percentage"] > topper["percentage"]:
            topper = student

    print("\n===== Class Topper =====")
    print("Name:", topper["name"])
    print("Roll Number:", topper["roll_number"])
    print("Percentage:", round(topper["percentage"], 2), "%")
    print("Grade:", topper["grade"])


# ----------------------------
# Class Average
# ----------------------------
def class_average():
    if len(students) == 0:
        print("\nNo Students Found.")
        return

    total_percentage = 0

    for student in students:
        total_percentage += student["percentage"]

    average = total_percentage / len(students)

    print("\nClass Average Percentage:", round(average, 2), "%")


# ----------------------------
# Main Program
# ----------------------------
while True:

    print("\n========== Student Grade Management System ==========")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Class Topper")
    print("7. Class Average")
    print("8. Exit")

    choice = input("Enter Your Choice (1-8): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        update_student()

    elif choice == "6":
        class_topper()

    elif choice == "7":
        class_average()

    elif choice == "8":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice! Please Try Again.")