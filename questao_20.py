"""
20) Leia um valor de massa em quilogramas e apresente-o convertido em libras.
A fórmula de conversão é: L = K/0.45, sendo K a massa em quilogramas
e L a massa em libras.
"""

K = float(input("Digite uma massa em quilogramas: "))

L = K / 0.45

print("A massa em Libras é: ", "%.2f" % L)