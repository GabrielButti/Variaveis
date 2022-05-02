"""
49) Faça um programa para ler o horário (hora, minuto e segundo)
de ínicio e duração em segundos, de uma experiência biológica.
O programa deve resultar com o novo horário (hora, minuto e segundo) do término da mesma.
"""

horaIn = int(input("Digite a Hora inicial: "))
minIn = int(input("Digite o Minuto inicial: "))
segIn = int(input("Digite o Segundo inicial: "))

print()

duracao = int(input("Digite a duração (Segundos): "))

horaDura = int(duracao / 3600)
minDura = int((duracao - (horaDura * 3600)) / 60)
segDura = int(duracao - (horaDura * 3600) - (minDura * 60))

horaFim = horaIn + horaDura
minFim = minIn + minDura
segFim = segIn + segDura

print("O término da experiência foi em: ","Hora(s)", horaFim, "|Minuto(s)", minFim, "|Segundo(s)", segFim)