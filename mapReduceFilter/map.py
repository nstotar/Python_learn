"""map syntax  map(function,iterable_obj)"""

l1 = [1,2,3,4,5]

def square(ele):
    return ele**2

result = map(square,l1)
res = list(result)


l2=['2','32','33','34']
nl = list(map(int,l2))
print(nl)
n2 = list(map(float,l2))
print(n2)