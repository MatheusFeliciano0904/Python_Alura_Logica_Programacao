# Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 2, 
# a tabuada deve ser mostrada no seguinte formato:

#         Tabuada do 2:
#         2 x 1 = 2
#         2 x 2 = 4
#         [...]
#         2 x 10 = 20


print("Informe um número para ser feita a tabuada: ")

num = int(input("Num: "))
i = 1

print("\n")
print(f"Tabuada do {num}: ")
for i in range(1, 11):
  
  print(f"{num} x {i} = {num*i}")

  i += 1
