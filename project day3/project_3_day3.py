expenses = []


def add_expense():
    item = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expense = {
        "Item": item,
        "Amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully!")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
    else:
        print("\n----- Expense List -----")
        for expense in expenses:
            print("Item :", expense["Item"])
            print("Amount :", expense["Amount"])
            print("-----------------------")


def total_expense():
    total = 0

    for expense in expenses:
        total += expense["Amount"]

    print("Total Expense = ₹", total)


while True:

    print("\n===== DAILY EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")