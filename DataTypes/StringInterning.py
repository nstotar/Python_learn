a='a1@z'
b='123za'
print("address of each char in 1st string")
for i,j in enumerate(a):
    print(f"1st string char '{j}' Address = {id(a[i])}")
for i,j in enumerate(b):
    print(f"2nd string char '{j}' Address = {id(b[i])}")