from math import radians, sin, cos, tan
print("=" *20)
ang = float(input(" Digite o ângulo que você deseja: "))
sen = sin(radians(ang))
print("=" *20)
print(f" o Ângulo de {ang} tem o SENO de {sen:.2f} ")
cosseno = cos(radians(ang))
print("=" *20)
print(f" o Ângulo de {ang} tem o COSSENO de {cosseno:.2f} ")
tan = tan(radians(ang))
print("=" *20)
print(f" o Ângulo de {ang} tem a TANGENTE de {tan:.2f}")

