"""
11) Leia uma velocidade em m/s (metros por segundo) e apresente-a
convertida em km/h (quilômetros por hora). A fórmula de conversão é: K = M * 3.6,
sendo K a velocidade km/h e M em m/s
"""

M = float(input("Digite uma velocidade em M/s: "))

K = M * 3.6

print("Velocidade em Km/h é: ", "%.2f" % K)