balance = 10000


def check_balance():
    print("\nYour Current Balance is: ₹", balance)


def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))
    balance = balance + amount
    print("Amount Deposited Successfully!")
    print("New Balance: ₹", balance)


def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= balance:
        balance = balance - amount
        print("Please collect your cash.")
        print("Remaining Balance: ₹", balance)
    else:
        print("Insufficient Balance!")


while True:

    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        print("Thank You for Using the ATM!")
        break

    else:
        print("Invalid Choice! Please Try Again.")