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
    [[8, 1], [7, 2], [2, 2], [4, 1], [1, 1]]
    >>> output = compress([1, 3, 3, 3, 3, 4, 5])
    >>> type(output)
    <class 'list'>
    >>> compress([5, 5, 3, 5, 5, 5])
    [[5, 2], [3, 1], [5, 3]]
    """
    compressed = []
    
    for i in range(len(input)):
        if i == 0 or input[i] != input[i-1]:
            count_zelfde = 0
            for j in range(i, len(input)):
                if input[j] != input[i]:
                    break
                count_zelfde += 1
    
            compressed.append([input[i], count_zelfde])
    
    return compressed

def decompress(input: list) -> list:
    """
    >>> decompress([[5, 3], [7, 2]])
    [5, 5, 5, 7, 7]
    >>> decompress([[5, 2], [3, 1], [5, 3]])
    [5, 5, 3, 5, 5, 5]
    >>> decompress([[0, 1], [-2, 2]])
    [0, -2, -2]
    >>> decompress([])
    []
    """
    decompressed = []
    
    for paar in input:
        for i in range(paar[1]):
            decompressed.append(paar[0])
    
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

if __name__ == "__main__":
    compressies = []
    for i in range(1000):
        integers = generate_integers()
        compressed_lijst = compress(integers)
        compressies.append(compression_ratio(compressed_lijst, integers))
    
        print(sum(compressies) / len(xs))
        