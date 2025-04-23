#converting data type from one type to other
a = 10
print("\nchecking data type of a that holds value 10",type(a))
print("\nCoverting int to float")
b=float(a)
print(f"value of int {a} changes to {b} {type(b)}")
# print("\n",type)
print("\nCoverting int to string")
c=str(a)
print(f" value of float {b} changes to '{c}' {type(c)}")
print("\nCoverting int to complex")
d=complex(a)
print(f" value of str '{c}' changes to {d} {type(d)}")

"""CONVERTING STRING TO INT HOLDING INTEGER VALUE"""
print(int('123'))
# print(int('123.22'))  ValueError: invalid literal for int() with base 10: '123.22'
# print(int('Code')) ValueError: invalid literal for int() with base 10: 'Code'
# print(int('True')) ValueError: invalid literal for int() with base 10: 'True'

# code to take a input from users in float and add them
a = float(input("Enter 1st number : "))
b = float(input("Enter 2nd number : "))
print(f"Addintion of {a} and {b} = {round(a+b,2)}")
# round off
print('{:.2f}'.format(78.8888))
print('{:.3f}'.format(123.567890987))


