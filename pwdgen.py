import random

"""
Hint: random.choice("abc")
"""

def new_password() -> str:
    """
    Genereert een wachtwoord
    """
    
    with open("no_offense.txt") as file:
    words = file.read().split("\n")
wordlist = []
for word in words:
    new_word = word.strip()
    if new_word != '':
        wordlist.append(new_word)
def print_avg_entropy() -> None:
    """
    Genereert 10.000 wachtwoorden en berekent gemiddelde entropie
    """

if __name__ == '__main__':
    print(new_password())
    print("Gemiddelde entropie van 10.000 nieuwe wachtwoorden is:")
    print_avg_entropy()