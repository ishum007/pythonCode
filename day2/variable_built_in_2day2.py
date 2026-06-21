first_name= "Ishika"
last_name= " Mahajan"
country= "India"
age= 19
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(age))

print(len(first_name))

print(len(first_name) > len(last_name))
 
num_one= 5
num_two= 4
total= num_one + num_two
diff= num_one - num_two
product= num_one * num_two
division= num_one / num_two
remainder= num_one % num_two
exponent= num_one ** num_two
floor_division= num_one // num_two
print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponent:", exponent)
print("Floor Division:", floor_division)

pi= 3.14
radius= 34
area_of_circle= pi * radius * radius
print("Area of circle:", area_of_circle)
circumference_of_circle= 2 * pi * radius
print("Circumference of circle:", circumference_of_circle)

r = float(input("Enter the radius of the circle: "))
area_of_circle = pi * r * r
print("Area of the circle with radius", r, "is:", area_of_circle)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print("Your full name is:", full_name)
country = input("Enter your country: ")
print("You are from", country)
age = int(input("Enter your age: "))
print("Your age is:", age)

help("keywords")
