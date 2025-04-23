d = {
    "name":"Nishant",
    "age":23,
    "phone":7899793325,
    "Science":98,
    "maths":30
}
print(d,type(d))

# accessing dict values with keys
print(d["name"])
print(d["phone"])

# iterating throughs keys 
print("\niterating throughs keys")
for i in d.keys():
    print(i,end=" ")
# iterating throughs values
print("\n\niterating throughs keys")
for i in d.values():
    print(i,end=" ")

# retrieving key as well as value from dictionary
print("\n\nretrieving key as well as value from dictionary")
for i in d.items():
    print(i,end=" ")