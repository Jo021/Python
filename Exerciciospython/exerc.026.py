frase = str(input("Digite uma frase: ")).upper().strip()
letras = frase.count("a")
primeira = frase.find("a")
ultima = frase.rfind("a")
print(f" A letra A apareceu na frase? {letras} vezes")
print(f" A posição de a na frase é: {primeira}")
print(f" A ultima posição da letra A foi {ultima}")


