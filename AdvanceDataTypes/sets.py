"""
1.Set is unordered collection of data.In does not maintain order of insertion
2.hetrogeneous collection of data
3.sets does not contain duplicate value
4.sets are mutable
"""
sets = {2,True, 6,5,"Nish"}
print(type(sets))
# Adding value to a set
sets.add(200)
print(sets)
# removing an element
print(sets.pop())

# removing perticular element
sets.remove("Nish")
print(sets)

# Union and intersection of a set
s1 = {1,2,3,4}
s2 = {'a','b',1,2}
print(f"union of {s1} and {s2} = {s1.union(s2)}")
print(f"intersection of {s1} and {s2} = {s1.intersection(s2)}")



