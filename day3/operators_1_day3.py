age = 19
height = 5.6
complex_num = 3 + 4j

base= float(input("enter base:"))
height= float(input("enter height:"))
area= 0.5* base* height
print("the area of the triangle is:", area)

a= float(input("enter side a:"))
b= float(input("enter side b:"))
c= float(input("enter side c:"))
perimeter= a + b + c
print("the perimeter of the triangle is:", perimeter)

length= float(input("enter length:"))
width= float(input("enter width:"))
area= length * width
perimeter= 2 * (length + width)
print("the area of the rectangle is:", area)
print("the perimeter of the rectangle is:", perimeter)

radius= float(input("enter radius:"))
pi= 3.14
area= pi * radius * radius
circumference= 2 * pi * radius
print("the area of the circle is:", area)
print("the circumference of the circle is:", circumference)

slope= 2
x_intercept= 3
y_intercept= -2
print("the slope of the line is:", slope)
print("the x-intercept of the line is:", x_intercept)
print("the y-intercept of the line is:", y_intercept)

x1, x2= 2, 4
y1, y2= 3, 5
slope= (y2 - y1) / (x2 - x1)
print("the slope of the line is:", slope)
distance= ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("the distance between the points is:", distance)

print("slope in task 8 is:",2)
print("slope in task 9 is:",2)
print(" both slopes are equal")
 
print(len("python"))
print(len("dragon"))
print(len("python") != len("dragon"))

print('on' in "python" and 'on' in "dragon")

sentence= "I hope this course is not full of jargon."
print('jargon' in sentence)

print('on' not in "python" and 'on' not in "dragon")

length= len("python")
print(length)
print(float(length))
print(str(length))

num= int(input("enter a number:"))
print("the number is even:", num % 2 == 0)

print(7//3== int(2.7))

print(type('10') == type(10))

print(int('9.8') == 10)

hours= int(input("enter hours:"))
rate_per_hour= int(input("enter rate per hour:"))
pay= hours * rate_per_hour
print("your weekly earning is:", pay)

years= int(input("enter number of years you have lived:"))
seconds= years * 365 * 24 * 60 * 60
print("you have lived for", seconds, "seconds")

