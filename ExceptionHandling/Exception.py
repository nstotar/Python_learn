def add(a,b):
    print(a/b)
    print("end")

try:
    add(10,10)
except:
    print("exceptioon occured and handled")
else:
    print("Exception is not occured")
finally:
    print("program Ended")