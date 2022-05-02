"""
15) Leia um ângulo em radianos e apresente-o convertido em graus.
A fórmula de conversão é: G = R * 180/r, sendo G o ângulo
em graus e R em radianos e r = 3.14.
"""

R = float(input("Digite um ângulo em radianos: "))

r = 3.14

G = R * 180 / r

print("O ângulo em graus é: ", "%.2f" % G)