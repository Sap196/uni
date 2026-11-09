import random

def generate_integers() -> int:
    """
    >>> output = generate_integers()
    >>> type(output)
    <class 'list'>
    >>> len(output)
    1000
    """
    integer_list = []
    
    for i in range(1000):
        getal = random.randint(0, 9)
        integer_list.append(getal)
    
    return integer_list
    
def compress(input: list) -> list:
    compressed = []
    
    return compressed