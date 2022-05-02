"""
17) Leia um valor de comprimento em centímetros e apresente-o convertida
em polegadas. A fórmula de conversão é: P = C / 2.54, sendo C o comprimento
em centímetros e P o comprimento em polegadas.
"""

C = float(input("Digite um comprimento em centímetros: "))

P = C / 2.54

print("O comprimento em polegadas é: ", "%.2f" % P)
