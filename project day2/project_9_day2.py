def unit_converter():

    print("===== Electricity Unit Converter =====")

    print("1. Watts to Kilowatts")
    print("2. Kilowatts to Watts")

    choice = int(input("Enter Your Choice (1-2): "))

    if choice == 1:
        watts = float(input("Enter Power in Watts: "))
        kilowatts = watts / 1000
        print("Power in Kilowatts =", kilowatts, "kW")

    elif choice == 2:
        kilowatts = float(input("Enter Power in Kilowatts: "))
        watts = kilowatts * 1000
        print("Power in Watts =", watts, "W")

    else:
        print("Invalid Choice")


unit_converter()