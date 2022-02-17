from random import shuffle

print(" Do mais gay ao menos gay")
pessoa1 = str(input(" Nome: "))
pessoa2 = str(input(" Nome: "))
pessoa3 = str(input(" Nome: "))
pessoa4 = str(input(" Nome: "))
pessoa5 = str(input(" Nome: "))
sorteio = [pessoa1, pessoa2, pessoa3, pessoa4, pessoa5]
shuffle(sorteio)
print(" A verdade é essa: ")
print("========RESULTADO=======")
print(f" {sorteio}")
