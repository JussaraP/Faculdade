'''Programa que solicite o raio e retorne o volume de uma esfera'''

import math

raio = float(input("Digite o valor do raio: "))

volume = (4 / 3) * math.pi * (raio ** 3)

print(f"O volume da esfera é: {volume}")