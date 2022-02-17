print("-" * 30)
num = int(input("Digite um número de 1 a 9999: "))
print("=" * 20)

Unidade = num // 1 % 10
Dezena = num // 10 % 10
Centena = num // 100 % 10
Milhar = num // 1000 % 10

print(f" A unidade de {num} é: {Unidade}")
print(f" A Dezena de {num} é: {Dezena}")
print(f" A Centena de {num} é: {Centena}")
print(f" A Milhar de {num} é: {Milhar} ")
print("=" * 20)
