# anotações de fundamentos da programação

## tipos de dados em python
1. string
2. number int
3. number float
4. boolean

## operadores matematicos - basicos
+-> adição 
--> subtração
*-> multiplicação
/-> divisão
## operadores lógicos
and-> e-> se duas condições forem verdadeiras , o resultado é verdadeiro.
or-> ou -> pelo menos uma condição foe verdadeira, o resultado é verdadeiro.
not-> ele altera o valor booliano da condição.

## metodos em python
1. print()-> exibe informações no terminal.
2. input() -> capturar uma informação no terminal.

## format em python

# estrutura de repetição
 ``if (se)`` -> verifica se uma condição é true (verdadeira) se for, ele executa o código.
 ``elif (senão se)`` -> é usado para testar arias condições .Ele só executa se todas as condições anteriores forem falsas
`` else (senão)`` -> executa o código se a condição for false (falsa).

# laços de repetição
é um recurso de programação que permite executar um conjunto de comando várias vezes, também são chamados de loop, laços de repetição ou iteração .
``FOR`` -> utilizamos quando sabemos quantas vezes queremos repetir algo sintax:
for variavel in range (inicio, fim)
   comandos
[range()]-> metodo que aceita geração de numeros
[inicio]-> é inclusivo . é o primeiro numero a ser usado
[fim] -> é exclusivo. o numero utilizado é o anterior a esse 
## Escopo variaveis
escopo local -> a variavel ela só é acessada dentro da estrutura que ela foi criada
``escopo global``-> a variavel pode ser acessada por todos 

## variaçoes das variaveis 
variavel em memoria -> é declarada quando voce não pretende utilizar essa variavel em outros cenarios 
variavel contadora -> é utilizada para uma logica onde uma repetição irá ser altereda.

`while`-> é utilizado quando não sabemos quantas vezes o programa vai repetir , ele repete enquanto uma condição for verdadeira
sintaxe:
while condicao:
    comandos 

## conversão de tipos em pyhton
1. int()-> a gente vai incluir qual variavel/dado que queremos converter para numero inteiro.
2. float()->  a gente vai incluir qual variavel/dado que queremos converter para numero decimal.
3. str()-> a gente vai incluir qual variavel/dado que queremos converter para texto.



## boas praticas
1. qualquer vaiavel em python utiliza o padrão de case snake_case ou recentemente o cammelcase.
2. se voce observar alguma estrutura tipo nome(), 90% de chance  de ser uma função. 
3. python não tem constante porem utilizamos o padrao case , uppercase, para simular que aquela variavel mão pode ser alter
