"""
50) Implemente um programa que calcule o ano de nascimmento
de uma pessoa a partir de sua idade e do ano atual.
"""

idade = int(input("Digite sua idadde: "))
anoAtual = int(input("Digite o ano atual: "))

anoNasc = anoAtual - idade

print("O ano de nascimento é: ", anoNasc)