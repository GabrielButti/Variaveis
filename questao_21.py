"""
21) Leia um valor de massa em libras e apresente-o convertido em quilogramas.
A fórmula de conversão é: K = L * 0.45, sendo K a massa em quilogramas e L a massa em libras.
"""

L = float(input("Digite a massa em libras: "))

K = L * 0.45

print("A massa em quilogramas é: ", "%.2f" % K)