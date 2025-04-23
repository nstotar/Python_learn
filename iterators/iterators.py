li= list(range(10,20,3))
iterator = iter(li)
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())   #StopIteration