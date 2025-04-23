def decor(function):
    def innerfunction(a,b):
        if b == 0:
            raise ZeroDivisionError
        else:
            return function(a,b)
    return innerfunction

@decor
def Div(a,b):
    print(f"Division of {a} ,{b} = {a/b}")
Div(10,3)
Div(10,2)
Div(10,0)