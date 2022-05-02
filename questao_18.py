"""
18) Leia um valor de um volume em metros cúbicos m³ e apresente-o
convertido em litros. A fórmula de conversão é: L = 1000 * M,
sendo L o volume em litros e M o volume em metros cúbicos
"""

M = float(input("Digite um volume em metros cúbicos: "))

L = 1000 * M

print("O volume em Litros é: ", "%.2f" % L)