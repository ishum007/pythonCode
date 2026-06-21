my_list =[]
print(my_list)

fruits = ['apple' , 'banana' , 'mango' , 'orange' , 'grapes' ,'watermelon']
print(fruits)
print(len(fruits))
print(fruits[0])
print(fruits[2])
print(fruits[-1])

mixed_data_types = ['Ishika', 19, 5.6, 'single', 'pathakot'] # name, age, height, marital status, address
print(mixed_data_types)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])

it_companies[0] = 'Meta'
print(it_companies)

it_companies.append('Twitter')
print(it_companies)

it_companies.insert(3, 'LinkedIn')
print(it_companies)

it_companies[1] =it_companies[1].upper()
print(it_companies)

result = '# '.join(it_companies)
print(result)

it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print('Google' in it_companies)# true
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[0:3])
print(it_companies[3:])
middle_company= it_companies[len(it_companies)//2]
print(middle_company)
it_companies.pop(0)
print(it_companies)
middle_company= len(it_companies)//2
print(middle_company)
it_companies.pop(middle_company)
print(it_companies)
it_companies.pop()
print(it_companies)
del it_companies


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_list = front_end + back_end
print(joined_list)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)