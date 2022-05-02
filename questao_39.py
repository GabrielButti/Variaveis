"""
39) A importância de R$ 780.000,00 será dividida entre três
ganhadores de um concurso. Sendo que da quantia total:
 - O primeiro ganhador receberá 46%;
 - O segundo receberá 32%;
 - O terceiro receberá o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores
"""

valor = 780000.00

prim = valor * 0.46
segu = valor * 0.32
terc = valor * 0.22

print("O primeiro ganhador ganhou: R$", "%.2f" % prim)
print("\nO segundo ganhador ganhou: R$", "%.2f" % segu)
print("\nO terceiro ganhador ganhou: R$", "%.2f" % terc)