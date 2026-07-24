def mobile_recharge():

    print("===== Mobile Recharge System =====")

    customer_name = input("Enter Customer Name: ")
    mobile_number = input("Enter Mobile Number: ")

    print("\nRecharge Plans")
    print("1. ₹199")
    print("2. ₹299")
    print("3. ₹399")
    print("4. ₹599")

    choice = int(input("Choose Recharge Plan (1-4): "))

    if choice == 1:
        amount = 199
        validity = "28 Days"

    elif choice == 2:
        amount = 299
        validity = "28 Days"

    elif choice == 3:
        amount = 399
        validity = "56 Days"

    elif choice == 4:
        amount = 599
        validity = "84 Days"

    else:
        print("Invalid Recharge Plan")
        return

    print("\n===== Recharge Successful =====")
    print("Customer Name :", customer_name)
    print("Mobile Number :", mobile_number)
    print("Recharge Amount : ₹", amount)
    print("Validity :", validity)
    print("Thank You!")


mobile_recharge()