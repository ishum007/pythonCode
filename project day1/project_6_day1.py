def calculate_salary():

    print("===== Employee Salary Calculator =====")

    name = input("Enter Employee Name: ")
    emp_id = input("Enter Employee ID: ")

    basic_salary = float(input("Enter Basic Salary: ₹"))

    hra = basic_salary * 0.20
    da = basic_salary * 0.10
    bonus = basic_salary * 0.05

    gross_salary = basic_salary + hra + da + bonus

    print("\n===== Salary Slip =====")
    print("Employee Name :", name)
    print("Employee ID   :", emp_id)
    print("Basic Salary  : ₹", basic_salary)
    print("HRA (20%)     : ₹", hra)
    print("DA (10%)      : ₹", da)
    print("Bonus (5%)    : ₹", bonus)
    print("Gross Salary  : ₹", gross_salary)


calculate_salary()