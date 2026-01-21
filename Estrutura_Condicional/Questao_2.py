""""
Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:

 Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
 Triângulo Equilátero: três lados iguais;
 Triângulo Isósceles: quaisquer dois lados iguais;
 Triângulo Escaleno: três lados diferentes;
"""


# ✅ Demandas do programa

# [✔] Solicitar à pessoa usuária três números que representem os lados do triângulo
# [✔] Validar se os valores informados podem formar um triângulo
# [✔] Informar se não é possível formar um triângulo (caso a regra não seja atendida)

# ✅ Classificação do triângulo (se for válido)

# [✔] Identificar se o triângulo é Equilátero (três lados iguais)
# [✔] Identificar se o triângulo é Isósceles (dois lados iguais)
# [✔] Identificar se o triângulo é Escaleno (três lados diferentes)


print("Informe os lado do triângulo")
lado_1 = float(input("Lado 1: "))
lado_2 = float(input("Lado 2: "))
lado_3 = float(input("Lado 3: "))

resultado = "sda"
if (lado_1 + lado_2) > lado_3:
  resultado = "positivo"
elif (lado_1 + lado_3) > lado_2:
  resultado = "positivo"
elif(lado_2 + lado_3) > lado_1:
  resultado = "positivo"
else:
  resultado = "negativo"

if resultado == "negativo":
  print("Não é possível formar um triângulo")
  exit()

print("\nTipo de triângulo:\n")
if lado_1 == lado_2 == lado_3:
  print("Triângulo Equilátero")
elif (lado_1 == lado_2) or (lado_1 == lado_3) or (lado_2 == lado_3):
  print("Triângulo Isósceles")
else:
  print("Triângulo Escaleno")
