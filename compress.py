import random

def generate_integers() -> int:
    integer_list = []
    
    for i in range(1000):
        getal = random.randint(1, 9)
        integer_list.append(getal)
    
    return integer_list