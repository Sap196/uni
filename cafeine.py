"""
Hoeveel koppen koffie? 2
Hoeveel koppen thee? 1
Hoeveel energiedrankjes? 0
Hoeveel glazen cola? 0
Je krijgt 225 mg cafeïne binnen.
"""

def calculate_cafeine(coffee: int, tea: int, energy: int, cola: int) -> int:
    """
    Berekent de hoeveelheid cafeine op basis van de hoeveelheid gedronken
      drankjes van het type koffie, thee, energie, en cola.
    """

if __name__ == '__main__':
    coffee = input("Hoeveel koppen koffie? ")
    tea = input("Hoeveel koppen thee? ")
    energy = input("Hoeveel energiedrankjes? ")
    cola = input("Hoeveel glazen cola? ")
    print(calculate_cafeine())