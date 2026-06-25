for i in range(11):
    print(i)

i = 0
while i < 11:
    print(i)
    i += 1

for i in range(10,-1,-1):
    print(i)

i = 10
while i > -1:
    print(i)
    i -= 1  

for i in range(1,8):
    print("#" * i)

for i in range(8):
    for j in range(8):
        print("#", end="")
    print()

for i in range(11):
    print(f"{i} x {i} = {i*i}")
     

languages =['python', 'numpy', 'pandas', 'django', 'flask']
for item in languages:
    print(item)

for i in range (0, 101):
    if i % 2 == 0:
        print(i)

for i in range (0, 101):
    if i % 2 != 0:
        print(i)

total = 0
for i in range (101):
    total  += i
print("the sum of all numbers is ", total)

even_sum = 0
odd_sum = 0
for i in range (101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("the sum of all evens are ", even_sum)
print("the sum of all odds are ", odd_sum )



fruits =[ 'banana', 'orange', 'mango', 'lemon']
for fruit in reversed (fruits):
    print(fruit)



      



