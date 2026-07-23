def calculate_fine():

    print("===== Library Fine Calculator =====")

    student_name = input("Enter Student Name: ")
    book_name = input("Enter Book Name: ")
    late_days = int(input("Enter Number of Late Days: "))

    if late_days <= 5:
        fine = late_days * 2

    elif late_days <= 10:
        fine = late_days * 5

    else:
        fine = late_days * 10

    print("\n===== Library Fine =====")
    print("Student Name :", student_name)
    print("Book Name    :", book_name)
    print("Late Days    :", late_days)
    print("Total Fine   : ₹", fine)


calculate_fine()