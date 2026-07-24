def shopping_bill():

    print("===== Shopping Mall Billing System =====")

    customer_name = input("Enter Customer Name: ")

    print("\nAvailable Products")
    print("1. Rice      - ₹60/kg")
    print("2. Sugar     - ₹45/kg")
    print("3. Oil       - ₹150/litre")
    print("4. Biscuits  - ₹30/packet")

    rice = int(input("\nEnter Quantity of Rice (kg): "))
    sugar = int(input("Enter Quantity of Sugar (kg): "))
    oil = int(input("Enter Quantity of Oil (litre): "))
    biscuits = int(input("Enter Quantity of Biscuits (packets): "))

    total = (rice * 60) + (sugar * 45) + (oil * 150) + (biscuits * 30)

    if total > 3000:
        discount = total * 0.10
    else:
        discount = 0

    final_bill = total - discount

    print("\n===== BILL =====")
    print("Customer Name :", customer_name)
    print("Total Amount  : ₹", total)
    print("Discount      : ₹", discount)
    print("Final Bill    : ₹", final_bill)


shopping_bill()