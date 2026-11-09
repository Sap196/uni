import random

def generate_integers() -> int:
    """
    >>>generate_integers()
    """
    integer_list = []
    
    for i in range(amount):
        getal = random.randint(0, 9)
        integer_list.append(getal)
    
    return integer_list