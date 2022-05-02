"""
24) Leia um valor de área em metros quadrados e m² e apresente-o
convertido em acres. A fórmula de conversão é: A = M * 0,000247, sendo M
a área em metros quadrados e A área em acres.
"""

M = float(input("Digite uma área em metros quadrados: "))

A = M * 0.000247

print("A área em acres é: ", "%.2f" % A)