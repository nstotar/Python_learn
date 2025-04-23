def auth_decorator(func):
    def wrapper():
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Hardcoded credentials
        if username == "admin" and password == "1234":
            print("Authentication successful.")
            func()
        else:
            print("Authentication failed. Access denied.")
    return wrapper

@auth_decorator
def secure_function():
    print("Hello, authenticated user!")

secure_function()
