"""
52) Três amigos jogaram na loteria. Caso eles ganhem,
o prêmio deve ser repartido porporcionalmente ao valor
que cada deu para a realização da aposta. Faça um programa
que leia quanto cada apostador investiu, o valor do prêmio,
e imprima quanto cada um ganharia do prêmio com base no valor investido.
"""

aposta1 = float(input("Digite o valor da primeira aposta: "))
aposta2 = float(input("Digite o valor da segunda aposta: "))
aposta3 = float(input("Digite o valor da terceira aposta: "))

print()

valorPremio = float(input("Digite o valor do prêmio: "))

print()

premio1 = (aposta1 + valorPremio / 3)
premio2 = (aposta2 + valorPremio / 3)
premio3 = (aposta3 + valorPremio / 3)

print("O primeiro apostador ganhará: ", "%.2f" % premio1)
print("O segundo apostador ganhará: ", "%.2f" % premio2)
print("O terceiro apostador ganhará: ", "%.2f" % premio3)
