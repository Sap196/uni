"""
$ python kalender.py
Jaar: 2022
Maand: 9
          Sep 2022
---------------------------
Zon Maa Din Woe Don Vri Zat
                  1   2   3
  4   5   6   7   8   9  10
 11  12  13  14  15  16  17
 18  19  20  21  22  23  24
 25  26  27  28  29  30
 """
 
# 1 januari 1800 is een woensdag
START_DAY = 3

def is_leap_year(year: int) -> bool:
    """
    Return True als `year` een schrikkeljaar is.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        
        return True
    
    return False
    
def days_from_1800(month: int, year: int) -> int:
    """
    Telt de dagen vanaf 1800 tot aan `month` of `year`.
    De eerste dag van `month` zit hier dus niet bij.
    Gebruikt `days_from_1800_until_year` en `days_until_month`.
    """
    dagen_vanaf_1800 = days_from_1800_until_year(year)
    dagen_tot_maand = days_until_month(month)
    
    return dagen_vanaf_1800 + dagen_tot_maand

def days_from_1800_until_year(year: int) -> int:
    """
    Telt de dagen vanaf 1800 tot aan `year`.
    1 januari van het nieuwe jaar is niet meegerekend.
    Gebruikt `is_leap_year`.
    """
    dagen = 0
    diff = year - 1800
    for i in range(diff):
        if is_leap_year(1800+i):
            dagen += 366
        if not is_leap_year(1800+i):
            dagen += 365
    
    return dagen
    
def days_until_month(month: int, year: int) -> int:
    """
    Telt het aantal dagen van 1 januari van `year` tot aan `month` van `year`.
    De dagen van `month` zitten hier dus niet bij.
    Gebruikt `days_in_month`.
    """
    dagen = 0
    for i in range(1, month):
        dagen += days_in_month(i, year)
    
    return dagen
    
def days_in_month(month: int, year: int) -> int:
    """
    Bepaalt het aantal dagen in `month` van `year`.
    Gebruikt `is_leap_year`.
    """
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return int(31)
    elif month in [4, 6, 9, 11]:
        return int(30)
    elif month == 2:
        if is_leap_year(year):
            return int(29)
        else:
            return int(28)

def display_calendar(month: int, year: int) -> None:
    """
    Print de kalender.
    Gebruikt `display_header` en `display_grid`.
    """
    print(display_header(month, year))
    print(display_grid(month, year))

def display_header(month: int, year: int) -> None:
    """
    Print de koptekst van de kalender.
    """
    months = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dec"]
    
    return f{"          " + months[month-1] + " " + str(year) + "\\n" + "---------------------------" + "\\n" + "Zon Maa Din Woe Don Vri Zat"}
def display_grid(month: int, year: int) -> None:
    """
    Print het grid van de kalender.
    Gebruikt `first_weekday_month` en `days_in_month`.
    """

def first_weekday_month(month: int, year: int) -> int:
    """
    Bepaalt de eerste weekdag van de maand.
    Gebruikt `days_from_1800`.
    """
    

if __name__ == '__main__':
    year = int(input("Jaar: "))
    month = int(input("Maand: "))
    #display_calendar(month, year)
    
    print(days_until_month(month, year))