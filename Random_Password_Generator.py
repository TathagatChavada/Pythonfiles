import random
import string

def generate_password(x):
    # Different characters of password
    str1 = string.ascii_letters
    str2 = string.digits
    str3 = string.punctuation

    str = str1 + str2 + str3

    # Looping over str using random function to generate password
    for i in range(0,l):
        print(random.choice(str),end='')
    print('\n')

# Length of password you want to generate.
l = int(input('Enter the length of password: '))
generate_password(l)