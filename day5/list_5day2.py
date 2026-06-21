ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort ()
print("Sorted ages:", ages)
print("Minimum age:", min(ages))
print("Maximum age:", max(ages))
ages .append(min(ages))
ages.append(max(ages))  
print("Ages after adding min and max:", ages)
ages.sort()
middle_1 = len(ages) // 2 -1
middle_2 = len(ages) // 2
median = (ages[middle_1] + ages[middle_2]) / 2
print("Median age:", median)

average = sum(ages) / len(ages)
print("Average age:", average)

range_of_ages = max(ages) - min(ages)
print("Range of ages:", range_of_ages)

print("abs(min(ages) - average):", abs(min(ages) - average))
print("abs(max(ages) - average):", abs(max(ages) - average))


countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle_country = len(countries) // 2
print("Middle country:", countries[middle_country])
mid = (len(countries) + 1) // 2
first_half = countries[:mid]
second_half = countries[mid:]
print("First half of the countries:", first_half)
print("Second half of the countries:", second_half)
china, russia, usa,*scandic_countries = countries
print("China:", china)
print("Russia:", russia)
print("USA:", usa)
print("Scandic countries:", scandic_countries)
