import math
print("=" *20)
n1 = float(input(" Informe o comprometo do cateto oposto: "))
n2 = float(input(" Informe o comprimento do cateto adjacente: "))

h1 = math.hypot(n1, n2)

print(f" a hipotenusa vai ser: {h1:.2f}")
print("=" *20)
