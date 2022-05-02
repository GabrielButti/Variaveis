"""
7) Leia uma temperatura em graus Fahrenheit e apresente-a convertida
em graus Celsius. A fórmula de conversão é: C = (F-32.0)*5.0/9.0,
sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.
"""

F = float(input("Digite uma temperatura em Fahrenheit: "))

C = (F-32.0)*5.0/9.0

print("O valor em Celsius é: ", "%.2f" % C)