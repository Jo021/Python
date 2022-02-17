real = float(input(" Quanto dinheiro você tem na carteira? R$"))
dolar = real / 5.26
euro = real / 6.02
print(f" Com R${real:.2f} você consegue comprar US{dolar:.2f}")
print(f" Com R${real:.2f} você consegue comprar EUR{euro:.2f}")
