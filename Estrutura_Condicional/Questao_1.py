"""
Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária 
qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o 
número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.
"""

# [✔] Ler dois números informados pela pessoa usuária
# [✔] Perguntar qual operação a pessoa usuária deseja realizar
# Exemplo: soma, subtração, multiplicação ou divisão
# [✔] Executar a operação escolhida
# [✔] Exibir o resultado da operação
##### Informações que o resultado deve apresentar #####
# [✔] Verificar se o número é par ou ímpar
# [✔] Verificar se o número é positivo ou negativo
# [✔] Verificar se o número é inteiro ou decimal

num1 = float(input("Informe o 1 número: "))
num2 = float(input("Informe o 2 número: "))

print("\n------------------------------ Operações ------------------------------\n")

print("+ - Adição")
print("- - Subtração")
print("* - Multiplicação")
print("/ - Divisão")

print("\n-----------------------------------------------------------------------\n")

operacao = input("Informe a operação: ")
print()
resultado = 0

match operacao:
  case "+":
    resultado = num1 + num2
  case "-":
    resultado = num1 - num2 
  case "*":
    resultado = num1 * num2
  case "/":
    resultado = num1 / num2

print(f"Resultado = {resultado}\n")

print("*********** Verificar se número é Par ou Ímpar ***********\n")

if resultado % 2 == 0:
  print(f"{resultado} é Par!")
else:
  print(f"{resultado} é impar")

print("\n*********** Verificar se número é Positivo ou Negativo ***********\n")

if resultado > 0:
  print(f"{resultado} é Positivo")
else:
  print(f"{resultado} é Negativo")


print("\n*********** Verificar se número é Inteiro ou Decimal ***********\n")

if resultado % 1 == 0 :
  print(f"{resultado} é Inteiro!")
else:
  print(f"{resultado} é Decimal")