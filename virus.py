import random
import string

def generate_virus(length:int) -> str:
    return str(random.choices("ACGT", k=length))
    
print(generate_virus(10))