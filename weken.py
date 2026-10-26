def weeks_elapsed(day1: int, day2: int) -> int:
    """
    Berekent het aantal volle weken dat verstreken is tussen twee dagen
    in hetzelfde jaar. De dagen zijn gegeven als dagnummer (day1 en day2).

    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2
    >>> weeks_elapsed(8, 5)

    >>> weeks_elapsed(40, 61)
    

    """
    return abs(day2 - day1) // 7

if __name__ == '__main__':
    day1 = int(input("Dagnummer 1: "))
    day2 = int(input("Dagnummer 2: "))
    result = weeks_elapsed(day1, day2)
    print(f"Er zijn {result} volle weken verstreken.")