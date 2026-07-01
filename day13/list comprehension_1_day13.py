numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

result = [num for num in numbers if num <= 0]

print(result)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened = [num for sublist in list_of_lists for num in sublist]

print(flattened)

countries = [[('Finland', 'Helsinki')],
             [('Sweden', 'Stockholm')],
             [('Norway', 'Oslo')]]

output = [
    [country.upper(), country[:3].upper(), city.upper()]
    for [(country, city)] in countries
]

print(output)

countries = [[('Finland', 'Helsinki')],
             [('Sweden', 'Stockholm')],
             [('Norway', 'Oslo')]]

output = [
    {
        'country': country.upper(),
        'city': city.upper()
    }
    for [(country, city)] in countries
]

print(output)



names = [[('Asabeneh', 'Yetayeh')],
         [('David', 'Smith')],
         [('Donald', 'Trump')],
         [('Bill', 'Gates')]]

output = [
    first + " " + last
    for [(first, last)] in names
]

print(output)



 # Lambda function to calculate slope
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

# Lambda function to calculate y-intercept (b = y - mx)
y_intercept = lambda x, y, m: y - (m * x)

# Example
m = slope(2, 3, 6, 11)
b = y_intercept(2, 3, m)

print("Slope:", m)
print("Y-intercept:", b)

result = [
    (i, i**0, i**1, i**2, i**3, i**4, i**5)
    for i in range(11)
]

print(result)