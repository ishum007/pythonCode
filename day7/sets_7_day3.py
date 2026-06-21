age =[22 , 18, 19, 25, 33, 45, 56, 79]
age_set = set(age)
print("length of list:" , len(age))
print("length of set:" , len(age_set))

if len(age) > len(age_set):
    print("list is bigger")
elif len(age) < len(age_set):
    print("set is bigger")
else:
    print("both are equal")

 

