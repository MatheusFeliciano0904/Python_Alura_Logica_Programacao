"""
Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:

O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.
"""


# ✅ Demandas de entrada

# [✔] Ler a quantidade de litros vendidos
# [✔] Ler o tipo de combustível
# [✔] E para etanol
# [✔] D para diesel

# ✅ Regras de preço por combustível

# [✔] Preço do etanol: R$ 1,70 por litro
# [✔] Preço do diesel: R$ 2,00 por litro

# ✅ Regras de desconto

# Etanol (E):

# [✔] Até 15 litros → desconto de 2% por litro
# [✔] Acima de 15 litros → desconto de 4% por litro

# Diesel (D):

# [✔] Até 15 litros → desconto de 3% por litro
# [✔] Acima de 15 litros → desconto de 5% por litro

# ✅ Cálculo do valor

# [✔] Calcular o valor do desconto
# [✔] Preço do litro × quantidade de litros × percentual de desconto
# [✔] Calcular o valor total sem desconto
# [✔] Preço do litro × quantidade de litros
# [✔] Calcular o valor final a ser pago
# [✔] Valor total − valor do desconto

# ✅ Saída do programa

# [✔] Exibir o valor final a ser pago pelo cliente



print("Informe a quantidade de litros vendidos:")
litros = float(input("Litros: "))
print("Informe o tipo de combustível:")
print("E - Etanol")
print("D - Diesel")
tipo = input("Tipo: ").upper()

if tipo == "E":
  if litros <= 15:
    desconto = 0.02
  else:
    desconto = 0.04
    
  preco_litro = 1.70
elif tipo == "D":
  if litros <= 15:
    desconto = 0.03
  else:
    desconto = 0.05

  preco_litro = 2.0

valor_desconto = preco_litro * litros * desconto
valor_total = preco_litro * litros
valor_final = valor_total - valor_desconto

print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor total: R$ {valor_total:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
