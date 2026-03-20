# estrutura de repetição
# if (se) -> verifica se uma condição é true (verdadeira) se for, ele executa o código.
# elif (senão se) -> é usado para testar arias condições .Ele só executa se todas as condições anteriores forem falsas
# else (senão) -> executa o código se a condição for false (falsa).

# idade_usuario = 9
# # se o usuario for maior de 18 anos , eu vou passar a informação: voce é maior de idade; senão voce é menor de idade
# if idade_usuario >= 18:
#     print("voce é maior de idade.") 
# else:
#     print("voce é menor de idade")

idade = 73
if idade >= 18:
    print("voce é maior de idade.")
elif idade >= 0 and idade < 18:
     print("voce é jovem de idade.")

elif idade >= 70:
      print("voce é experiente de idade.")
else:
      print("voce é menor de idade.")