def grocery_bill():

    print("===== Grocery Bill Calculator =====")

    customer_name = input("Enter Customer Name: ")

    item1 = input("Enter Item 1 Name: ")
    price1 = float(input("Enter Price of Item 1: "))
    quantity1 = int(input("Enter Quantity of Item 1: "))

    item2 = input("Enter Item 2 Name: ")
    price2 = float(input("Enter Price of Item 2: "))
    quantity2 = int(input("Enter Quantity of Item 2: "))

    item3 = input("Enter Item 3 Name: ")
    price3 = float(input("Enter Price of Item 3: "))
    quantity3 = int(input("Enter Quantity of Item 3: "))

    total = (price1 * quantity1) + (price2 * quantity2) + (price3 * quantity3)

    
    if total >= 1000:
        discount = total * 0.10
    else:
        discount = 0

    final_bill = total - discount

    print("\n===== BILL =====")
    print("Customer Name :", customer_name)
    print("Total Amount  : ₹", total)
    print("Discount      : ₹", discount)
    print("Final Bill    : ₹", final_bill)


grocery_bill()