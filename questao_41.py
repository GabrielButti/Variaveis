"""
41) Faça um programa que leia o valor da hora de trabalho (em reais)
e número de horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário.
Adicionando 10% sobre o valor calculado.
"""

valorHora = float(input("Digite o valor da hora: "))
horasTrab = float(input("Digite a quantidade de horas trabalhadas: "))

ValorPago = valorHora * horasTrab
valorPago += valorPago * 0.10

print("O valor a ser pago é: R$", "%.2f" % valorPago)