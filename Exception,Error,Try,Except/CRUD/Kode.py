import random
import string

def string_format(angka:int)-> str:
    return ''.join(random.choice(string.ascii_letters) for i in range(angka))