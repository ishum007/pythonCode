def bmi_calculator():

    print("===== BMI Calculator =====")

    name = input("Enter Your Name: ")
    weight = float(input("Enter Weight (kg): "))
    height = float(input("Enter Height (m): "))

    bmi = weight / (height * height)

    if bmi < 18.5:
        status = "Underweight"
    elif bmi < 25:
        status = "Normal Weight"
    elif bmi < 30:
        status = "Overweight"
    else:
        status = "Obese"

    print("\n===== BMI REPORT =====")
    print("Name        :", name)
    print("Weight      :", weight, "kg")
    print("Height      :", height, "m")
    print("BMI         :", round(bmi, 2))
    print("Category    :", status)


bmi_calculator()