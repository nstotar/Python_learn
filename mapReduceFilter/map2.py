li = list(eval(input("Enter comma sap values: ")))
print("Original Value: ",li)

def sqr(i):
    return i**2

nlist=list(map(sqr,li))
print("New List: ",nlist)