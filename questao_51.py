"""
51) Escreva um programa que leia as coordenadas x e y de pontos
no R² e calcule sua distância da origem (0, 0)
"""

import math

X = int(input("Digite a coordenada x: "))
Y = int(input("Digite a coordenada y: "))

resultado = math.sqrt(math.pow(X, 2) + math.pow(Y, 2))

print("A distância da origem é: ", "%.1f" % resultado)