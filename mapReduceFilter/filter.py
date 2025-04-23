# l1= list(eval(input("Enter comma separeted Elements: ")))
# print("Original List",l1)
# def even(ele):
#     if ele%2==0:
#         return ele

# even_li = list(filter(even,l1))
# print(even_li)

li = list(eval(input("Enter comma sep value: ")))
print("Original List:",li)

def even(i):
    if i%2==0:
        return i
even_ele=list(filter(even,li))
print("evenList",even_ele)