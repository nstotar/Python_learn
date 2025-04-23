if 3 ==3:
    print("1st result matched")
elif 2==2:
    print("sec result matched")
else:
    print("invalid condition")

for i in range(1,11):
    print(i,end = ",")
# code to understand the working of continue statement
print()
for i in range(1,11):
    if(i==3):
        continue
    print(i,end = ",")
# code to understand the break working
print()
a=1
while(a<10):
    if(a==5):
        break
    print(a,end=",")
    a+=1
# code to print Multiplication table
num = int(input("\nEnter the number  to generate its table: "))
for i in range(1,11):
    print(num*i,end = " ")

# PASS keyword Usage in empty methods
# its allow us to define an empty method
def nish():
    pass