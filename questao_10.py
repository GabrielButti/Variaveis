"""
10) Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida
em m/s (metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade
em km/h e M em m/s.
"""

K = float(input("Digite uma velocidade em Km/h: "))

M = K/3.6

print("Velocidade em M/s é:", "%.2f" % M)