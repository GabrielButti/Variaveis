"""
32) Leia um número inteiro e imprima a soma do sucessor
de seu triplo com o antecessor e seu dobro.
"""

num = int(input("Digite um número inteiro: "))

suce = (num * 3) + 1
ante = (num * 2) - 1

print("A soma é:", suce + ante)

