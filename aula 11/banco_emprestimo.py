print ("sistema de emprestimo bancario")

# entrada de dados
idade= int (input( "digite a idade do cliente : ") )
salario= float (input("digite o salario do cliente :"))
tempo_trabalho= int (input("digite o tempo de trabalho (em anos):") )

# estruturas condicionais
if idade < 18:
    print("emprestimo negado. cliente menor de idade.")
elif salario >= 5000:
    print("emprestimo aprovado automaticamente.")
elif idade >= 18 and salario >= 2000 and tempo_trabalho>= 2:
     print("emprestimo aprovado.")
else:
    print("emprestimo negado.")
 # verificar a idade, o salario e o tempo de trabalho
