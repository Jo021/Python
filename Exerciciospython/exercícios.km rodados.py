print("=" *16)
dias = int(input("Quantos dias alugados? "))
print("=" *16)
km = float(input("Quantos Km rodados? "))
valor = (dias * 60) + (km * 0.15)
print("=" *16)
print(f" o Valor a ser cobrado será R${valor:.2f}")
print("=" *16)
