"""
27) Leia um  valor de área em hectares e apresente-o convertido em
metros quadrados m². A fórmula de conversão é: M = H * 10000,
sendo M a área em metros quadrados e H a área em hectares.
"""

H = float(input("Digite uma área em hectares: "))

M = H * 10000

print("A área em metros quadrados é: ", "%.2f" % M)