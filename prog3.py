inp = input("Geef getal: ")
try:
    inp = int(inp)
    print(abs(inp))
except:
    print("Geef een getal als input.")