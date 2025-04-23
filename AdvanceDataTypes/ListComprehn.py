li=[10,20,30,40]
sq=[]
for i in li:
    sq.append(i**2)
print(sq)

# list comprehension
"""Syntax for list comphrehension
[return_expression for iterable_variable in(membership oprator) interable_object ]
        sql = [i**2 for i in li]
"""
sql = [i**2 for i in li]
print(sql)

print( [i+5  for i in li])
l1 = [ 1,2,3,4,5,6,7,8,9]
print ([i for i in l1 if i%2==0])


