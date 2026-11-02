import random

"""
Hint: random.choice("abc")
"""

def new_password() -> str:
    """
    Genereert een wachtwoord
    """
    
    # de offensieve woordenlijst laden
    with open("no_offense.txt") as file:
        words = file.read().split("\n")
    wordlist = []
    for word in words:
        new_word = word.strip()
        if new_word != '':
            wordlist.append(new_word)
    
    
    # het wachtwoord genereren
    hoofdletter = random.randint(1,3)
    nummer = random.randint(1,5)
    
    while nummer == hoofdletter:
        nummer = random.randint(1,5)
    
    # wachtwoord genereren
    output = ""
    
    if hoofdletter == 1:
        output+= return_char(0).upper()
    else:
        output+= return_char(0)
    
    output+= return_char(1) # char 2
    output+= return_char(0) # char 3
    output+= return_char(0) # char 4
    if nummer == 2:
        output+= return_char(2) # char 5
    else:
        output+= return_char(1) # char 5
    output+= "-"            # char 6
    
    if hoofdletter == 2:
        output+= return_char(0).upper()
    elif nummer == 2
    else:
        output+= return_char(0)

def return_char(type: int) -> str:
    """
    Type 0 geeft consonants
    Type 1 geeft vowel
    Type 2 geeft getal
    """
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
    'n', 'p', 'r', 's', 't', 'v', 'w', 'q', 'z']
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    
    if type == 0:
        out = random.choice(consonants)
    elif type == 1:
        out = random.choice(vowels)
    elif type == 2:
        out = random.randint(1,9)
    
    return str(out)

def print_avg_entropy() -> None:
    """
    Genereert 10.000 wachtwoorden en berekent gemiddelde entropie
    """

if __name__ == '__main__':
    print(new_password())
    print("Gemiddelde entropie van 10.000 nieuwe wachtwoorden is:")
    print_avg_entropy()