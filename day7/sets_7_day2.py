# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("union of A and B:" , A.union(B))
print("intersection of A and B:" , A.intersection(B))
print("is A subset of B?" , A.issubset(B))
print("are A and B disjoint?" , A.isdisjoint(B))
print("A union B:" , A.union(B))
print("B union A:" , B.union(A))
print("symmetric difference between A and B:" , A.symmetric_difference(B))
del A
del B