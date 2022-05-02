"""
23) Leia um valor de comprimento em metros e apresente-o convertido em jardas.
a fórmula de conversão é: J = M/0.91, snedo J o comprimento em jardas e
M o comprimento em metros.
"""

M = float(input("Digite um comprimento em metros: "))

J = M / 0.91

print("O comprimento em jardas é: ", "%.2f" % J)