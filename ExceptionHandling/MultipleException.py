def add(a,b):
    print(a/b)

try:
    add(10,2)
    add(10,int('abc'))
except ZeroDivisionError:
    print("Zero Division Error")
except ValueError:
    print("error:ValueError")
except TypeError:
    print("Type Error")
