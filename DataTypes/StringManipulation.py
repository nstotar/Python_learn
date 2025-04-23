s1 = "Nishant is here"
print("The total length of string \"Nishant is here\" = ",len(s1))
for i,j in enumerate(s1):
    print(f"index is: {i} and latter at s1[{i}] = {j}")

#String scliesing
print(s1[1:4])
print(s1[:4])
print(s1[::-1])

#checking the ids of two strings
s1 = "Hello"
s2 = "World"
print(f"String :->{s1} is stored at {id(s1)} this address")
print(f"String :->{s2} is stored at {id(s2)} this address")
print(f"String s1[4] ie o :->{s1[4]} is stored at {id(s1[4])} this address")
print(f"String s2[3] ie o :->{s1[1]} is stored at {id(s1[1])} this address")
print(f"\nAddress of s1[2],s1[3]:={id(s1[2])}, {id(s1[3])}")
print(f"Address of s1[1]:={id(s2[1])}")