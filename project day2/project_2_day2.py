def restaurant_bill():

    print("===== Restaurant Bill Calculator =====")

    customer_name = input("Enter Customer Name: ")

    print("\n----- MENU -----")
    print("1. Burger      - ₹150")
    print("2. Pizza       - ₹300")
    print("3. Pasta       - ₹200")
    print("4. Cold Drink  - ₹50")

    burger = int(input("\nEnter Quantity of Burger: "))
    pizza = int(input("Enter Quantity of Pizza: "))
    pasta = int(input("Enter Quantity of Pasta: "))
    cold_drink = int(input("Enter Quantity of Cold Drink: "))

    total = (burger * 150) + (pizza * 300) + (pasta * 200) + (cold_drink * 50)

    
    gst = total * 0.05

    final_bill = total + gst

    print("\n===== BILL =====")
    print("Customer Name :", customer_name)
    print("Total Amount  : ₹", total)
    print("GST (5%)      : ₹", gst)
    print("Final Bill    : ₹", final_bill)


restaurant_bill()