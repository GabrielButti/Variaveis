"""
40) Uma empresa contrata um encanador a R$30,00 por dia.
Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima
a quantida liquida que deverá ser paga. Sabendo-se que são descontandos 8% para imposto de renda.
"""

dias = int(input("Digite a quantidade de dias de serviço: "))

salario = dias * 30.00
salarioTotal = salario - (salario * 0.08)

print("Deverá ser pago: R$", "%.2f" % salarioTotal)