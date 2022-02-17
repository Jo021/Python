largura = float(input(" Informe a largura da parede: "))
altura = float(input("informe a altura da parede: "))
area = largura * altura
print("-" * 30)
print(f" sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m² ")
tinta = area / 2
print(f" Para pintar essa parede você precisar de {tinta}l de tinta")
print("-" * 30)
