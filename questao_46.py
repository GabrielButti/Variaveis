"""
46) Faça um programa que leia um número inteiro positivo de
três digitos (de 100 a 999). Gere outro número formado pelos
dígitos invertidos do número lido. Exemplo:

    NúmeroLido = 123
    NúmeroGerado = 321
"""

num = int(input("Digite um número: "))

numGerado = str(num)[::-1]

print("O número gerado: ", numGerado)