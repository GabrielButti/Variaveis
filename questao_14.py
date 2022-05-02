"""
14) Leia um ângulo em graus e apresente-o convertido em radianos.
A fórmula de conversão é: R = G * r / 180, sendo G o ângulo em graus
e R em radianos e r = 3.14.
"""

G = float(input("Digite um ângulo em graus: "))

r = 3.14

R = G * r / 180

print("O ângulo em radianos é: ", "%.2f" % R)