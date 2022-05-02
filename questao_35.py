"""
35) Sejam a e b os catetos de um triângulo, onde a hipotenusa
é obtida pela equação: hipotenusa = √a² + √b². Faça um
programa que receba os valores de a e b e calcule o valor
da hipotenusa através da equação. Imprima o resultado dessa operação.
"""

A = float(input("Digite o valor do cateto A: "))
B = float(input("Digite o valor do cateto B: "))

hipo = (A ** 2 + B ** 2) ** 0.5

print("A hipotenusa é: ", "%.2f" % hipo)

