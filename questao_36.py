"""
36) Leia a altura e o raio de um cilindro círcular e imprima
o volume do cilindro. O volume de um cilindro circular é calculado por meio
da seguinte fórmula: V = r * raio² * altura, onde r = 3.141592
"""

alt = float(input("Digite a altura de um cílindro círcular: "))
raio = float(input("Digite o raio de um cílindro círcular: "))

r = 3.141592
V = r * (raio ** 2) * alt

print("O volume do cílindro é: ", "%.2f" % V)