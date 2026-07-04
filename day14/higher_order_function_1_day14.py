from functools import reduce

numbers = [1,2,3,4,5]

def square(x):
    return x*x

def even(x):
    return x%2==0

def add(x,y):
    return x+y

print(list(map(square,numbers)))
print(list(filter(even,numbers)))
print(reduce(add,numbers))
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for country in countries:
    print(country)

for name in names:
    print(name)

for num in numbers:
    print(num)

uppercase = list(map(str.upper, countries))
print(uppercase)

square = list(map(lambda x: x**2, numbers))
print(square)

upper_names = list(map(str.upper, names))
print(upper_names)

land = list(filter(lambda x: "land" in x, countries))
print(land)

six = list(filter(lambda x: len(x)==6, countries))
print(six)

six_more = list(filter(lambda x: len(x)>=6, countries))
print(six_more)


e_country = list(filter(lambda x: x.startswith("E"), countries))
print(e_country)

from functools import reduce

result = reduce(
    lambda x,y:x+y,
    filter(
        lambda x:x>10,
        map(lambda x:x*x,numbers)
    )
)

print(result)


def get_string_lists(lst):
    return list(filter(lambda x:isinstance(x,str),lst))

print(get_string_lists([1,"Python",2,"AI",True]))

from functools import reduce

total = reduce(lambda x,y:x+y,numbers)
print(total)

sentence = ", ".join(countries[:-1]) + ", and " + countries[-1] + " are north European countries."

print(sentence)

def categorize_countries(pattern):
    return list(filter(lambda x: pattern.lower() in x.lower(), countries))

print(categorize_countries("land"))
def starting_letter_count(countries):
    result = {}

    for country in countries:
        first = country[0]

        if first in result:
            result[first]+=1
        else:
            result[first]=1

    return result

print(starting_letter_count(countries))
def get_first_ten_countries(countries):
    return countries[:10]

print(get_first_ten_countries(countries))
def get_last_ten_countries(countries):
    return countries[-10:]

print(get_last_ten_countries(countries))
