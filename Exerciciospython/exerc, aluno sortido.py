import random
print(" Qual deles é o melhor?")
alun1 = str(input(" Primeiro(a): "))
alun2 = str(input(" Segundo(a): "))
alun3 = str(input(" Terceiro(a): "))
alun4 = str(input(" Quarto(a): "))
alun5 = str(input(" Quinto(a): "))
lista = [alun1, alun2, alun3, alun4, alun5]
escolhido = random.choice(lista)
print(f" {escolhido} é o melhor"!)
