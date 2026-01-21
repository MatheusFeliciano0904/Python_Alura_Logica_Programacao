"""
Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa 
que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos 
de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.
"""

print("********* distribuição de idades de pensionistas de uma empresa *********\n")

idade = 1
faixa_1 = 0
faixa_2 = 0
faixa_3 = 0
faixa_4 = 0


while idade > 0:

  idade = int(input("Informe a idade:"))

  if idade > 0 and idade < 25:
    faixa_1 += 1
  elif idade >= 26 and idade < 50:
    faixa_2 += 1
  elif idade >= 51 and idade < 75:
    faixa_3 += 1
  elif idade >= 76 and idade <= 100:
    faixa_4 += 1
  else:
    print("Idade inválida")


print(f"Distribuição em intervalos de [0-25] = {faixa_1}")
print(f"Distribuição em intervalos de [26-50] = {faixa_2}") 
print(f"Distribuição em intervalos de [51-75] = {faixa_3}") 
print(f"Distribuição em intervalos de [76-100] = {faixa_4}")  
