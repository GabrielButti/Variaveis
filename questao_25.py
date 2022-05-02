"""
25) Leia um valor de área em acres e apresente-o convertido
em metros quadrados m². A fórmula da conversão é: M = A*4048.58,
sendo M a área em metros quadrados e A a área em acres
"""

A = float(input("Digite uma área em acres: "))

M = A * 4048.58

print("A área em metros quadrados é: ", "%.2f" % M)