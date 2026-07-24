def bus_ticket():

    print("===== Bus Ticket Booking System =====")

    passenger_name = input("Enter Passenger Name: ")

    print("\nAvailable Destinations")
    print("1. Delhi      - ₹500")
    print("2. Chandigarh - ₹300")
    print("3. Amritsar   - ₹250")
    print("4. Pathankot  - ₹150")

    choice = int(input("\nChoose Destination (1-4): "))
    tickets = int(input("Enter Number of Tickets: "))

    if choice == 1:
        destination = "Delhi"
        fare = 500

    elif choice == 2:
        destination = "Chandigarh"
        fare = 300

    elif choice == 3:
        destination = "Amritsar"
        fare = 250

    elif choice == 4:
        destination = "Pathankot"
        fare = 150

    else:
        print("Invalid Destination")
        return

    total_bill = fare * tickets

    print("\n===== Ticket Details =====")
    print("Passenger Name :", passenger_name)
    print("Destination    :", destination)
    print("Fare Per Ticket: ₹", fare)
    print("No. of Tickets :", tickets)
    print("Total Bill     : ₹", total_bill)
    print("Thank You! Have a Safe Journey.")


bus_ticket()