"""
43) Escreva um programa de ajuda para vendedores. A partir de um valor
total lido, mostre:
 - O total a pagar com desconto de 10%
 - O valor de cada parcela, no parcelamento de 3x sem juros;
 - A comissão do vendedor, no caso da venda ser a vista(5% sobre o valor com desconto)
 - A comissão do vendedor, no caso da venda ser parcelada(5% sobre o valor total)
"""

valorTotal = float(input("Digite um valor total: "))

desconto = valorTotal - (valorTotal * 0.10)
parcela = valorTotal / 3
comiVista = (desconto * 0.05)
comiPar = (valorTotal * 0.05)

print("\nO total a pagar com o desconto de 10% é: R$", "%.2f" % desconto)
print("O valor de cada parcela é: R$", "%.2f" % parcela)
print("A comissão do vendedor por venda a vista é: R$", "%.2f" % comiVista)
print("A comissão do vendedor por venda parcelada é: R$", "%.2f" % comiPar)