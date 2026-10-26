inp = input("Geef getal: ")
try:
    inp = int(inp)
except:
    print("Geef een getal als input.")
print(abs(inp))