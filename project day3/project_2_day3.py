passwords = {}


def add_password():
    website = input("Enter website name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    passwords[website] = {
        "Username": username,
        "Password": password
    }

    print("Password saved successfully!")


def view_passwords():
    if len(passwords) == 0:
        print("No passwords saved.")
    else:
        print("\nSaved Passwords:")
        for website, details in passwords.items():
            print("Website :", website)
            print("Username:", details["Username"])
            print("Password:", details["Password"])
            print("-----------------------")


def search_password():
    website = input("Enter website name: ")

    if website in passwords:
        print("Username:", passwords[website]["Username"])
        print("Password:", passwords[website]["Password"])
    else:
        print("Website not found.")


def delete_password():
    website = input("Enter website name to delete: ")

    if website in passwords:
        del passwords[website]
        print("Password deleted successfully.")
    else:
        print("Website not found.")


while True:

    print("\n===== PASSWORD MANAGER =====")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Search Password")
    print("4. Delete Password")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_password()

    elif choice == "2":
        view_passwords()

    elif choice == "3":
        search_password()

    elif choice == "4":
        delete_password()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")