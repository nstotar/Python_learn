def decor(function):
    def inner(name): #name parameter
        if name == "Ayush":
            print(name,"Likes Biryani")
        else:
            return function(name)
    return inner
@decor
def process(name):
    print(name,'likes pilao')

process('Ankit')  
process('Nisa')
process('Ayush')#name parameter
process('Raju')
