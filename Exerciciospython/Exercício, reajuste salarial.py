preçopro = float(input(" Informe o preço do produto: R$"))

avista = preçopro - (preçopro * 10 / 100)
parcelado = preçopro + (preçopro * 20 / 100)
print("=" * 20)
print(f" O valor de R${preçopro:.2f} a vista fica: R${avista:.2f}")
print(f" O valor de R${preçopro:.2f} parcelado fica: R${parcelado:.2f}")
print("=" * 20)
