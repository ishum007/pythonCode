age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print("You are not old enough to learn to drive.")

my_age = 20
your_age = int(input("Enter your age: "))
if your_age > my_age:
    difference = your_age - my_age
    if difference == 1:
        print("you are 1 year older than me.")
    else:
        print(f"you are {difference} years older than me.")
elif your_age < my_age:
    difference = my_age - your_age
    if difference == 1:
        print("you are 1 year older than me.")
    else:
        print(f"you are {difference} years older than me.")
else:
    print("We are the same age.")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if a > b:
    print(f"{a} is greater than {b}.")
elif a < b:
    print(f"{a} is less than {b}.")
else:
    print(f"{a} is equal to {b}.")

score = int(input("Enter your score: "))
if 90 <= score <= 100:
    print("Your grade is A.")
elif 80 <= score < 90:
    print("Your grade is B.")
elif 70 <= score < 80: 
    print("Your grade is C.")
elif 60 <= score < 70:
    print("Your grade is D.")
else:
    print("Your grade is F.")

month = input("Enter the month: ")
if month in ["September", "October", "November"]:
    print("The season is Autumn.")
elif month in ["December", "January", "February"]:
    print("The season is Winter.")
elif month in ["March", "April", "May"]:
    print("The season is Spring.")
elif month in ["June", "July", "August"]:
    print("The season is Summer.")
else:
    print("Invalid month.")

fruits = ["banana", "orange", "mango", "lemon"]
fruit = input("Enter a fruit: ")
if fruit in fruits:
    print(f"{fruit} is in the list.")
else:
    fruits.append(fruit)
print("Updated fruits list:", fruits)


person ={
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_married": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {
        "street": "Space street",
        "zipcode": "02210"
    }
}
if "skills" in person:
    skills = person["skills"]
    middle = len(skills) // 2
    print("Middle skill:", skills[middle])
    if "Python" in skills:
        print("The person has Python skill.")
    if skills == ["JavaScript", "React"]:
        print("The person has only JavaScript and React skills.")
    elif skills ==['node', 'Python', 'MongoDB']:
         print("The person has only Node, Python and MongoDB skills.")
    elif 'react' in skills and 'Node' in skills and 'MongoDB' in skills:
        print("The person has React, Node and MongoDB skills.")
    else:
        print("The person has other skills as well.")

    if person["is_married"] and person["country"] == "Finland":
        print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
        