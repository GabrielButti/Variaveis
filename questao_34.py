"""
34) Leia o valor do raio de um círculo e calcule e imprima área do círculo
correspondente. A área do círculo é r * raio², conside r = 3.141592
"""

raio = float(input("Digite o valor do raio de um círculo: "))

r = 3.141592
area = r * (raio * raio)

print("A área do círculo é: ", "%.2f" % area)