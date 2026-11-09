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

def decompress(input: list) - > list:
    decompressed = []
    
    return decompressed

def compression_ratio(compressed: list, original: list) -> int:
    """
    >>> compression_ratio([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [[]])
    
    """
    compression_ratio_number = (len(uncompressed) / (len(compressed) * 2))
    
    return compression_ratio_number