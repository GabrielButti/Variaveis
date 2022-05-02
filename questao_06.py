"""
6) Leia uma temperatura em graus Celsius e apresente-a convertida
em graus Fahrenheit. A fórmula de conversão é: F = C*(9.0/5.0)+32,
sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""

C = float(input("Digite uma temperatura em Celsius: "))

F = C *(9.0/5.0)+32

print("O valor em Fahrenheit é: ", "%.2f" % F)