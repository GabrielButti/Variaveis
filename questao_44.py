"""
44) Receba a altura do degrau de uma escada e a altura que o usuário
deseja alcançar subindo a escada. Calcule e mostre quantos degraus o usuário
deverá subir para atingir seu objetivo.
"""

altDe = float(input("Digite a altura do degrau (cm): "))
altUs = float(input("Digite a altura do usuário (m): "))

quantDeg = int((altUs * 100) / altDe)

print("A quantidade de degraus é: ", quantDeg)