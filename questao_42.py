"""
42) Receba o salário-base de um funcionário. Calcule e imprima o salário
a receber, sabendo-se que esse funcionário tem gratificação de 5% sobre o salário-base.
Além disso, ele paga 7% de imposto sobre o salário-base.
"""

salaBase = float(input("Digite o salário-base: "))

salaTotal = salaBase + (salaBase * 0.05)
salaTotal -= salaBase * 0.07

print("O salário a receber é: R$", "%.2f" % salaTotal)