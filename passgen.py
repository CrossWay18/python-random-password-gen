import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+"

while 1:
    password_len = int(input("how long do you want ya password to be? : "))
    password_count = int(input("how many passwords do you want? : "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password      = password + password_char
        print("here is the password :" ,password)
