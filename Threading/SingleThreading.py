import time
def print_numbers():
    for i in range(1,6):
        print(i)
        time.sleep(1)

def print_characters():
    for i in ['A','B','C','D']:
        print(i)
        time.sleep(1)
        
print_numbers()
print_characters()