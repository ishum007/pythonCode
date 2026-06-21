family_member =( 'sibling', 'father' , 'mother' )
print("family_member:" , family_member)
print("sibling :" , family_member[0])
print("father :" , family_member[0])
print("mother :" , family_member[1])

fruits = ('apple' , 'banana' , 'orange')
vegetables = ('carrot' , 'potato' , 'onion')
animal_products = ('milk' , 'meat' , 'butter')
food_stuff_tp = fruits + vegetables + animal_products
print("food_stuff_tp:" , food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print("food_stuff_lt:" , food_stuff_lt)

middle = len(food_stuff_tp) // 2
print("middle item:" , food_stuff_tp[middle])
print("first three items:" , food_stuff_tp[:3])
print("last three items:" , food_stuff_tp[-3:])

del food_stuff_tp

nordic_countries = ('Denmark' , 'Finland' , 'Iceland' , 'Norway' , 'Sweden')
print("Is 'Estonia' a nordic country?" , 'Estonia' in nordic_countries)
print("Is 'Iceland' a nordic country?" , 'Iceland' in nordic_countries)
