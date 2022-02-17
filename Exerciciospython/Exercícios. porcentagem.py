preço = float(input(" Digite um valor de produto R$"))
np = preço - (preço * 5 / 100)
print(f" o valor R${preço:.2f} com 5% de desconto é igual a: R${np:.2f} ")