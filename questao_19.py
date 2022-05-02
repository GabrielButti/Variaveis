"""
19) Leia um valor de um volume em litros e apresente-o
convertido em metros cúbicos m³. A fórmula de conversão é: M = L/1000,
sendo o L o volume em litros e M o volume em metros cúbicos.
"""

L = float(input("Digite um volume em Litros: "))

M = L / 1000

print("O volume em metros cubicos é: ", "%.2f " % M)