s1 = "  Nish  "
print(s1.strip(" "))
s2 = "__Nish__"
print(s2.strip("_"))
print(s2.lstrip("_"))
print(s2.rstrip("_"))
print("\t ADDITION TAKING INPUT FROM USERs")
n1 = int(input("Enetr first Number : "))
n2 = int(input("Enetr Second Number : "))
print(f"Addition of  {n1} and {n2} = {n1+n2}")

# strip all the blank spaces and read the input from usres
str1 = input("Enter your name ")
print("before strip")
print(str1)
str2 = input("Enter your name ").strip()
print("AFTER STRIP")
print(str2)

#finding the index of a given index in a string
s1 = "nishant Totar learning coding at Kodnest"
print(s1.find("at"))