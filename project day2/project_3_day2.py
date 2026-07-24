def bank_interest():

    print("===== Bank Interest Calculator =====")

    customer_name = input("Enter Customer Name: ")
    principal = float(input("Enter Principal Amount (₹): "))
    rate = float(input("Enter Rate of Interest (%): "))
    time = float(input("Enter Time (Years): "))

    
    simple_interest = (principal * rate * time) / 100

    
    total_amount = principal + simple_interest

    print("\n===== BANK DETAILS =====")
    print("Customer Name    :", customer_name)
    print("Principal Amount : ₹", principal)
    print("Rate of Interest :", rate, "%")
    print("Time             :", time, "Years")
    print("Simple Interest  : ₹", simple_interest)
    print("Total Amount     : ₹", total_amount)


bank_interest()