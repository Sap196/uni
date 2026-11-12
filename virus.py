import random
import string

def generate_virus(length:int) -> str:
    return random.choice("ACGT", k=length)
    
print (generate_virus(10))