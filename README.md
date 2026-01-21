# RELEMBRANDO CONCEITOS

# Algumas Questões em Python:

###### Estruturas de Condição


## Questão 1
```
Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual
operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número -
se é par ou ímpar, positivo ou negativo e inteiro ou decimal.
```
## Questão 2
```
Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo.
O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo,
 se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:

Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
```
## Questão 3
```
Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:

O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.
```
## Questão 4
```
Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:

Para variação acima de 20%: bonificação para o time de vendas.
Para variação entre 2% e 20%: pequena bonificação para time de vendas.
Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
Para bonificações abaixo de -10%: corte de gastos.
```


###### Estruturas de Repetição


## Questão 1
```
Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:

        Tabuada do 2:
        2 x 1 = 2
        2 x 2 = 4
        [...]
        2 x 10 = 20

```
## Questão 2
```
Os números primos possuem várias aplicações dentro da Ciência de Dados, por exemplo, na criptografia e segurança. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
```
## Questão 3
```
Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.

```

## Questão 4
```
Em uma eleição para gerência em uma empresa com 20 funcionários, existem quatro candidatos. Escreva um programa que calcule o vencedor da eleição. A votação ocorreu da seguinte maneira:

Cada funcionário votou em um dos quatro candidatos (representados pelos números 1, 2, 3 e 4).
Também foram contabilizados os votos nulos (representado pelo número 5) e os votos em branco (representado pelo número 6).
Ao final da votação, o programa deve exibir o total de votos para cada candidato, o número de votos nulos e o número de votos em branco. Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.

```

###### Estruturas de Dados

## Questão 1
```
Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o número de bactérias por dia (em milhares) e pode ser observado a seguir: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Tendo esses valores, faça um código que gere uma lista contendo o percentual de crescimento de bactérias por dia, comparando o número de bactérias em cada dia com o número de bactérias do dia anterior. Dica: para calcular o percentual de crescimento usamos a seguinte equação: 100 * (amostra_atual - amostra_passada) / (amostra_passada).

```

## Questão 2

```
Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.

```


## Questão 3

```
Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta foi igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.

Gabarito da prova:
01 - D
02 - A
03 - C
04 - B
05 - A
06 - D
07 - C
08 - C
09 - A
10 - B

```


## Questão 4

```
Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).

```


## Questão 5

```
Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário:

{'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

```



## Questão 6

```
Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças. A pesquisa foi feita e o votos computados podem ser observados abaixo:

'''
Tabela de votos da marca
Design 1 - 1334 votos
Design 2 - 982 votos
Design 3 - 1751 votos
Design 4 - 210 votos
Design 5 - 1811 votos
'''


```
