"""
Os números primos possuem várias aplicações dentro da Ciência de Dados, por exemplo, na criptografia e segurança.
Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro 
e determine se ele é ou não um número primo.
"""

num = int(input("Digite um número: "))

for i in range(2, num):
  if (num % i) == 0:
    print(f"{num} é primo")
    break

else:
  print(f"{num} não é primo")