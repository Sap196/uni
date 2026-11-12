import random
import string

def generate_virus(length:int) -> str:
    return "".join(random.choices("ACGT", k=length))
    
def mutate(virus: str) -> str:
    
