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
    """
    >>> compress([1, 3, 3, 3, 3, 4, 5])
    [[1, 1], [3, 4], [4, 1], [5, 1]]
    >>> compress([8, 7, 7, 2, 2, 4, 1])
    [[1, 1], [3, 4], [4, 1], [5, 1]]
    >>> compress([1, 3, 3, 3, 3, 4, 5])
    [[1, 1], [3, 4], [4, 1], [5, 1]]
    """
    compressed = []
    
    for i in range(len(input)):
        if not input[i] == input[i-1]:
            count_zelfde = 0
            if not i == (len(input) - 1):
                for j in range(i, len(input)):
                    if input[i] == input[j]:
                        count_zelfde += 1
                    else:
                        compressed.append([input[i], count_zelfde])
                        break
            else:
                compressed.append([input[i], 1])
    
    return compressed

def decompress(input: list) -> list:
    decompressed = []
    
    return decompressed

def compression_ratio(compressed: list, original: list) -> int:
    """
    >>> compression_ratio([[5, 4], [7, 4]], [5, 5, 5, 5, 7, 7, 7, 7])
    2.0
    >>> compression_ratio([[5, 2]], [5, 5])
    1.0
    >>> compression_ratio([[5, 1], [7, 1]], [5, 7])
    0.5
    """
    
    compression_ratio_number = (len(original) / (len(compressed) * 2))
    
    return compression_ratio_number

print(compress([1, 3, 3, 3, 3, 4, 5]))