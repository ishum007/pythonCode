def movie_ticket():

    print("===== Movie Ticket Booking System =====")

    customer_name = input("Enter Customer Name: ")

    print("\nAvailable Movies")
    print("1. Kabhu Khushi Kabhie Gham - ₹250")
    print("2. Yeah Jawani Hai Deewani - ₹200")
    print("3. Saiyaara - ₹180")

    choice = int(input("\nChoose Movie (1-3): "))
    tickets = int(input("Enter Number of Tickets: "))

    if choice == 1:
        movie = "kabhu khushi kabhie gham"
        price = 250

    elif choice == 2:
        movie = "Yeah jawani hai deewani"
        price = 200

    elif choice == 3:
        movie = "Saiyaara"
        price = 180

    else:
        print("Invalid Choice")
        return

    total = price * tickets

    if tickets > 5:
        discount = total * 0.10
    else:
        discount = 0

    final_bill = total - discount

    print("\n===== Movie Ticket =====")
    print("Customer Name :", customer_name)
    print("Movie Name    :", movie)
    print("Ticket Price  : ₹", price)
    print("No. of Tickets:", tickets)
    print("Total Amount  : ₹", total)
    print("Discount      : ₹", discount)
    print("Final Bill    : ₹", final_bill)



movie_ticket()