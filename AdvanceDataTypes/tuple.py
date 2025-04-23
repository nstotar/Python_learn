tup = (10,20,20,"true",True)

""" ---FEATURES---
1. order of elements
2.immutable
3.hetrogeneous values 
4.it can hold duplicate values
"""
print(tup[0])

# unpacking tuple
e1,e2,e3,e4,e5=tup
print(f"e1:{e1}, e2:{e2}, e3:{e3}, e4:{e4}, e5:{e5}")

# TUPLE concatination
t1 = (10,20)
t2 = ("Nishant","Totar")
con = t1+t2
print(con)

# finding length of a tuple
t1=(1,2,3,4)
print(len(t1))