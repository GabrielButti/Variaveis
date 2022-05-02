"""
22) Leia um valor de comprimeto em jardas e apresente-o convertido em metros.
A fórmula de conversão é: M = 0.91 * J, sendo J o comprimeto em jardas
e M o comprimeto em metros.
"""

J = float(input("Digite o comprimento em jardas: "))

M = J * 0.91

print("O comprimento em metros é: ", "%.2f" % M)