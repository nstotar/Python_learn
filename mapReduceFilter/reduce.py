from functools import reduce
li = list(range(1,15,2))
print("list Elements: ",li)
def add(a,b):
    return a+b

sum_result = reduce(add,li)
print(sum_result)

# FINDING FACTORIAL-----------
n=int(input("Enter number to find its factorial using reduce function: "))
li = list(range(1,n+1))

def mul(a,b):
    return a*b

factprial = reduce(mul,li)
print(f"factorial of {n} is {factprial}")
