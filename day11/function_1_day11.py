def add_two_numbers(num1 ,num2):
    return num1+num2
result = add_two_numbers(10, 20)
print("sum:" , result)
 
def area_of_circle(radius):
    pi = 3.14159
    return pi*radius*radius
print(area_of_circle(45))

def add_all_nums(*args):
    total =0
    for num in args:
        if not isinstance(num,(int,float)):
            return "error: all arguments must be numbers ."
        total += num
        return total
    print(add_all_nums(2,3,4,5))

def convert_celsius_to_fahrenheit(c):
    return(c*9/5)+ 32
print(convert_celsius_to_fahrenheit(30))

def check_season(month):
    month=month.lower()
    if month in ["december","january",'february']:
        return"winter"
    elif["march","april","may"]:
        return"spring"
    elif["june","july","august"]:
        return"summer"
    elif["september","october","november"]:
        return"autum"
    else:
        return"invaild month"
print(check_season("september"))

def calculate_slope(x1,x2,y1,y2):
    if x2-x1 ==0:
     return"slope is undefined"
    return(y2-y1)/(x2-x1)
print(calculate_slope(2,3,4,7))

import math
def solve_quadratic_equation(a,b,c):
    d=b**2-4*a*c
    if d>0:
        x1=(-b +math.sqrt(d))/(2*a)
        x2=(-b -math.sqrt(d))/(2*a)
        return"x1,x2"
    elif d==0:
        x=-b/(2*a)
        return x
    else:
        return"no real roots"
print(solve_quadratic_equation(1,-5,6))

def print_list(lst):
     for item in lst:
        print(item)
print_list([1,2,3,4,5])

def reverse_list(lst):
    result=[]
    for i in range(len(lst)-1,-1,-1):
        result.append(lst[i])
    return result
print(reverse_list([1,2,3,4,5]))
print(reverse_list(['A','B','C','D']))

def capitalize_list_items(lst):
    result = []

    for item in lst:
        result.append(item.capitalize())

    return result

print(capitalize_list_items(["apple", "banana", "mango"]))

def add_item(lst, item):
    lst.append(item)
    return lst

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, 'Meat'))

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

def sum_of_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

print(sum_of_numbers(5))
print(sum_of_numbers(10))

def sum_of_odds(n):
    total = 0

    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i

    return total

print(sum_of_odds(10))

def sum_of_even(n):
    total = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i

    return total

print(sum_of_even(10))

def evens_and_odds(n):
    even = 0
    odd = 0

    for i in range(n + 1):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    print("The number of odds are:", odd)
    print("The number of evens are:", even)

evens_and_odds(100)

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact

print(factorial(5))

def is_empty(value):
    if value:
        return False
    else:
        return True

print(is_empty([]))
print(is_empty([1, 2]))
print(is_empty(""))
print(is_empty("Python"))

def calculate_mean(lst):
    return sum(lst) / len(lst)

numbers = [2, 4, 6, 8, 10]
print(calculate_mean(numbers))

def calculate_median(lst):
    lst.sort()
    n = len(lst)

    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

numbers = [2, 4, 6, 8, 10]
print(calculate_median(numbers))

def calculate_mode(lst):
    return max(set(lst), key=lst.count)

numbers = [2, 3, 3, 4, 5, 3]
print(calculate_mode(numbers))

def calculate_range(lst):
    return max(lst) - min(lst)

numbers = [2, 4, 6, 8, 10]
print(calculate_range(numbers))

def calculate_variance(lst):
    mean = sum(lst) / len(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    return variance

numbers = [2, 4, 6, 8, 10]
print(calculate_variance(numbers))

import math

def calculate_std(lst):
    mean = sum(lst) / len(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    return math.sqrt(variance)

numbers = [2, 4, 6, 8, 10]
print(calculate_std(numbers))

def greet(name="Guest"):
    print("Hello,", name + "!")

greet()
greet("Ishika")

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

print(is_prime(7))
print(is_prime(10))

def is_unique(lst):
    if len(lst) == len(set(lst)):
        return True
    else:
        return False

print(is_unique([1, 2, 3, 4]))
print(is_unique([1, 2, 2, 4]))

def same_data_type(lst):
    first_type = type(lst[0])

    for item in lst:
        if type(item) != first_type:
            return False

    return True

print(same_data_type([1, 2, 3]))
print(same_data_type([1, "2", 3]))

def is_valid_variable(name):
    return name.isidentifier()

print(is_valid_variable("first_name"))
print(is_valid_variable("1name"))
print(is_valid_variable("myName"))
      
import countries

def most_spoken_languages(n):
    language_count = {}

    for country in countries:
        for language in country['languages']:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1

    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)

    return sorted_languages[:n]

print(most_spoken_languages(10))

import countries

def most_populated_countries(n):
    sorted_countries = sorted(
        countries,
        key=lambda country: country['population'],
        reverse=True
    )

    return sorted_countries[:n]

print(most_populated_countries(10))

def show_args(**kwargs):
    if not kwargs:
        print("No arguments were provided.")
    else:
        for key, value in kwargs.items():
            print(f"{key}: {value}")


# Example 1
show_args(name="Alice", age=30, city="New York")

# Output:
# name: Alice
# age: 30
# city: New York

# Example 2
show_args(name="Bob", pet="Fluffy, the bunny")

# Output:
# name: Bob
# pet: Fluffy, the bunny


