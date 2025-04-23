li=[10]
print("\tBefore appending a list: ",li)  #Before appending a list:  [10]

# Append method will add the element at end of a list """
li.append(100)
print("\tAfter appending 100:",li)  
#After appending 100: [10, 100]


                    # Insert method helps to insert an eliment at specified index
li.insert(1,"Nishant")  
print("\tAfter inserting 'Nishant' @ index-1 :",li)     
#After inserting 'Nishant' @ index-1 : [10, 'Nishant', 100]


                    # pop method remove the last element
print("\tThe pop method element removed last value and returns that value:",li.pop())   
#The pop method element removed last value and returns that value: 100

print("\t",li) 
#[10, 'Nishant']
                        
                         # pop method remove the given index value
print("\tThe pop method element removed last value and returns that value:",li.pop(0)) 
#The pop method element removed last value and returns that value: 10

print("\t",li) 
# ['Nishant']

                        # remove method removes the matching element from the list
li.remove("Nishant")   
print("\t",li)       #     []

# --------------------------------------Appending some values becoz list is empty ----------------------------------
li.append(100)
li.append(88)
li.append(2.20)
li.append("Nish")
print(li)
# -------------------------------------------------------------------------------------------------------------------

                        # del method to remove element

#delete the element from specified index 
del(li[0])
print(li) 