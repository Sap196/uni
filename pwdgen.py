import random, math

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
    output+= return_char(1) # char 5
    
    if nummer == 2:
        output+= return_char(2) # char 6
    else:
        output+= return_char(1) # char 6
    output+= "-"            # char 7
    
    if hoofdletter == 2:
        output+= return_char(0).upper() # char 8
    elif nummer == 3:
        output+= return_char(2) # char 8
    else:
        output+= return_char(0) # char 8

    output+= return_char(1) # char 9
    output+= return_char(0) # char 10
    output+= return_char(0) # char 11
    output+= return_char(1) # char 12

    if nummer == 4:
        output+= return_char(2) # char 13
    else:
        output+= return_char(1) # char 13
    output+= "-"            # char 14
    
    if hoofdletter == 3:
        output+= return_char(0).upper() # char 15
    elif nummer == 5:
        output+= return_char(2) # char 15
    else:
        output+= return_char(0) # char 15

    output+= return_char(1) # char 16
    output+= return_char(0) # char 17
    output+= return_char(0) # char 18
    output+= return_char(1) # char 19

    if nummer == 6:
        output+= return_char(2) # char 20
    else:
        output+= return_char(1) # char 20
        
    
    return str(output)
    
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
    print(lengte * math.log2(aantal_tekens))

if __name__ == '__main__':
    outp = new_password()
    print(outp)
    print("Gemiddelde entropie van 10.000 nieuwe wachtwoorden is:")
    print_avg_entropy(outp)