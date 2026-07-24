def exam_eligibility():

    print("===== Exam Eligibility Checker =====")

    student_name = input("Enter Student Name: ")
    roll_number = input("Enter Roll Number: ")

    attendance = float(input("Enter Attendance Percentage: "))
    internal_marks = float(input("Enter Internal Marks (Out of 30): "))

    if attendance >= 75 and internal_marks >= 12:
        status = "Eligible for Exam"
    else:
        status = "Not Eligible for Exam"

    print("\n===== Student Details =====")
    print("Student Name          :", student_name)
    print("Roll Number           :", roll_number)
    print("Attendance Percentage :", attendance, "%")
    print("Internal Marks        :", internal_marks)
    print("Status                :", status)


exam_eligibility()