"""
Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:

Para variação acima de 20%: bonificação para o time de vendas.
Para variação entre 2% e 20%: pequena bonificação para time de vendas.
Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
Para bonificações abaixo de -10%: corte de gastos.
"""


# ✅ Demandas de entrada de dados

# [✔] Coletar a quantidade de vendas do ano de 2022
# [✔] Coletar a quantidade de vendas do ano de 2023

# ✅ Cálculo da variação percentual

# [✔] Calcular a variação percentual de vendas entre 2022 e 2023
# [✔] Fórmula:

# \text{Variação (%) } = \frac{(\text{Vendas 2023} - \text{Vendas 2022})}{\text{Vendas 2022}} \times 100
# ✅ Regras de decisão (sugestões)

# [✔] Variação acima de 20%
# [✔] Sugerir bonificação para o time de vendas
# [✔] Variação entre 2% e 20%
# [✔] Sugerir pequena bonificação para o time de vendas
# [✔] Variação entre 2% e -10%
# [✔] Sugerir planejamento de políticas de incentivo às vendas
# [✔] Variação abaixo de -10%
# [✔] Sugerir corte de gastos

# ✅ Saída do programa

# [✔] Exibir o percentual de variação calculado
# [✔] Exibir a sugestão correspondente para a diretoria


print("Informe a quantidade de vendas do ano de 2022:")
vendas_2022 = float(input("Vendas: "))
print("Informe a quantidade de vendas do ano de 2023:")
vendas_2023 = float(input("Vendas: "))

variacao = ((vendas_2023 - vendas_2022) / vendas_2022) * 100

if variacao > 20:
  print("Sugestão: Bonificação para o time de vendas")
  print(f"Variação: {variacao:.2f}%")
  exit()
elif 2 <= variacao <= 20:
  print("Sugestão: Pequena bonificação para o time de vendas")
  print(f"Variação: {variacao:.2f}%")
  exit()
elif -10 <= variacao < 2:
  print("Sugestão: Planejamento de políticas de incentivo às vendas")
  print(f"Variação: {variacao:.2f}%")
  exit()

print("Sugestão: Corte de gastos")
print(f"Variação: {variacao:.2f}%")
