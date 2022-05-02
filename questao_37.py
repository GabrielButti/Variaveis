"""
37) Faça um programa que leia o valor de um produto e imprima
o valor com desconto, tendo em vista que o desconto foi de 12%.
"""

valor = float(input("Digite o valor do produto: "))
desc = valor - (valor * 0.12)

print("O valor com desconto é: ", "%.2f" % desc)