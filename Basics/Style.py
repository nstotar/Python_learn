print("Hello World..!")
#Performing addition in scripting style:
print("Performing addition in scripting style")
a,b=10,20
print(f"addition of {a} and {b} = {a+b}")
"""python is dynamically typed programmers no need to mention the data type
python is most concise programming language"""

#performing addition in procedural way
print("performing addition in procedural style")
def addtion(a,b):
    print("Sum is : ",a+b)
addtion(a,b)
#object oriented style
class sum:
    a,b=10,20
    add = a+b
obj=sum()
print("object oriented style",obj.add)