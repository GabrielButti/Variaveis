"""
8) Leia uma temperatura em graus Kelvin e apresente-a convertida em
graus Celsius. A fórmula de conversão é: C = K - 273,15,
sendo C a temperatura em Celsius e K a temperatura em Kelvin.
"""

K = float(input("Digite uma temperatura em Kelvin: "))

C = K - 273.15

print("A temperatura em Celsius é: ", "%.2f" % C)