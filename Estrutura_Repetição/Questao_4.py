"""
Em uma eleição para gerência em uma empresa com 20 funcionários, existem quatro candidatos. Escreva 
um programa que calcule o vencedor da eleição. A votação ocorreu da seguinte maneira:

Cada funcionário votou em um dos quatro candidatos (representados pelos números 1, 2, 3 e 4).
Também foram contabilizados os votos nulos (representado pelo número 5) e os votos em branco (representado pelo número 6).
Ao final da votação, o programa deve exibir o total de votos para cada candidato, o número de votos nulos e o número de votos em branco.
Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.

"""

print("********* eleição para gerência em uma empresa com 20 funcionários *********\n")

candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
candidato_4 = 0
voto_nulo = 0
voto_branco = 0

while voto > 0:
  voto = int(input("Informe o número do candidato: "))
  if voto == 1:
    candidato_1 += 1
  elif voto == 2:
    candidato_2 += 1
  elif voto == 3:
    candidato_3 += 1
  elif voto == 4:
    candidato_4 += 1
  elif voto == 5:
    voto_nulo += 1
  elif voto == 6:
    voto_branco += 1
  else:
    print("Voto inválido")

print(f"Total de votos para candidato 1 = {candidato_1}")
print(f"Total de votos para candidato 2 = {candidato_2}")
print(f"Total de votos para candidato 3 = {candidato_3}")
print(f"Total de votos para candidato 4 = {candidato_4}")
print(f"Total de votos nulos = {voto_nulo}")
print(f"Total de votos em branco = {voto_branco}")

# Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.

total_votos = candidato_1 + candidato_2 + candidato_3 + candidato_4 + voto_nulo + voto_branco

porcentagem_voto_nulo = (voto_nulo / total_votos) * 100
porcentagem_voto_branco = (voto_branco / total_votos) * 100

print(f"Porcentagem de votos nulos = {porcentagem_voto_nulo}")
print(f"Porcentagem de votos em branco = {porcentagem_voto_branco}")
