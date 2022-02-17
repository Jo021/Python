nome = str(input("Digite seu nome: ")).strip()
print(" Analisando seu nome...")
print(f" Seu nome em Maísculas é: {nome.upper()}")
print(f" Seu nome em Minusculas é: {nome.lower()}")
espaços = nome.count(" ")
print(f" Seu nome tem ao todo: {len(nome) - espaços}")
print(f" Seu primeiro nome tem: {nome.find(' ')}")

