"""
38) Leia o salário de um funcionário. Calcule e imprima o valor do novo salário,
sabendo que ele recebeu um aumento de 25%.
"""

salario = float(input("Digite o valor do salário: "))
aument = salario + (salario * 0.25)

print("Novo salário: ", "%.2f" % aument)