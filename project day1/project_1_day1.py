# Function to calculate grade
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

# Main Function
def student_result():

    print("===== Student Result Calculator =====")

    # Input
    name = input("Enter Student Name: ")

    english = float(input("Enter English Marks: "))
    maths = float(input("Enter Maths Marks: "))
    science = float(input("Enter Science Marks: "))
    computer = float(input("Enter Computer Marks: "))
    hindi = float(input("Enter Hindi Marks: "))

    # Calculate total and percentage
    total = english + maths + science + computer + hindi
    percentage = (total / 500) * 100

    # Calculate grade
    grade = calculate_grade(percentage)

    # Pass or Fail
    if percentage >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    # Display Result
    print("\n===== RESULT =====")
    print("Student Name :", name)
    print("Total Marks  :", total, "/500")
    print("Percentage   :", round(percentage, 2), "%")
    print("Grade        :", grade)
    print("Result       :", result)

# Call the function
student_result()