class InvalidAge(Exception):
    pass
def checkAge(age):
    if age<18:
        raise InvalidAge("Age Must be greater than 18")
    else:
        print("Good to knowthat you are an Adult")
n = int(input("Enter your Age: "))
try:
    checkAge(n)
except InvalidAge as e:
    print("Exception occored details are :",e)