def calculate_bill(units):

    if units <= 100:
        bill = units * 5

    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)

    else:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    return bill



def electricity_bill():

    print("===== Electricity Bill Calculator =====")

    customer_name = input("Enter Customer Name: ")
    units = int(input("Enter Units Consumed: "))

    total_bill = calculate_bill(units)

    print("\n===== BILL =====")
    print("Customer Name :", customer_name)
    print("Units Consumed:", units)
    print("Total Bill    : ₹", total_bill)



electricity_bill()