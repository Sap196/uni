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
      
    >>> calculate_cafeine(1, 0, 1, 0)
    
    """
    return coffee * 90 + tea * 45 + energy * 80 + cola * 40

if __name__ == '__main__':
    coffee = int(input("Hoeveel koppen koffie? "))
    tea = int(input("Hoeveel koppen thee? "))
    energy = int(input("Hoeveel energiedrankjes? "))
    cola = int(input("Hoeveel glazen cola? "))
    print(calculate_cafeine(coffee, tea, energy, cola))