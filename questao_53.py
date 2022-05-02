"""
53) Faça umm programa para ler as dimensões de um terreno
(comprimento c e largura l), bem como o preço do metro de tela p.
Imprima o custo para cercar este mesmo terreno com tela.
"""

C = float(input("Digite o comprimento do terreno: "))
L = float(input("Digite a largura do terreno: "))
P = float(input("Digite o preço do metro de tela: "))

area = C * L
precoTela = area * P

print("O preço para cercar o terreno é: ", "%.2f" % precoTela)
