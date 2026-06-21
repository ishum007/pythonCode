print('thirty'+ ' ' + 'days'+ ' '+ 'of' + ' ' + 'python')

print('coding'+ ' ' + 'for'+ ' '+ 'all')

company= "coding for all"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:6])
print(company.find('coding'))
print('coding'in company)
print(company.replace('coding', 'python'))
text = 'python for everyone'
print(text.replace('everyone', 'all'))
print(company.split())
compaines = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(compaines.split(','))
print(company[0])
print(len(company) - 1)
company= "coding for all"
print(company[10])
text= "python for everyone"
acronym= text[0] + text[7] + text[11]
print(acronym)
text="coding for all"
acronym= text[0] + text[7] + text[11]
print(acronym)
company= "coding for all"
print(company.index('c'))
print(company.index('f'))
sentence= "You cannot end a sentence with because because because is a conjunction"
print(sentence.index('because'))
print(sentence.rindex('because'))
print(sentence[31:54])
company= "coding for all"
print(company.startswith('coding'))
print(company.endswith('coding'))
company= "   coding for all   "
print(company.strip())
print("30 days of python".isidentifier())
print("thirty_days_of_python".isidentifier())
  
library= ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'.join(library))

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

radius= 10
area= 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius,int(area)))

radius= 10
area= 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {int(area)} meters square.")

a= 8
b= 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
