"""
48) Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos
"""

seg = int(input("Digite um valor em segundos: "))

min = int(seg / 60)

hora = int(min / 60)

print("Hora(s):", hora, "|Minuto(s):", min, "|Segundo(s):", seg)