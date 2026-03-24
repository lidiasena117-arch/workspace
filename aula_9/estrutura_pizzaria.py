#variaveia da pizzaria 
pizza_sabor= input("informe o sabor da pizza - [frango com requeijão], [calabresa], [mussarela], [banana com chocolate]:")
pizza_tamanh0= input("informe o tamanho da pizza - [pequena], [medio], [grande]:")
dia_semana= input("informe o dia da semana - [quarta], [quinta], [sexta] ,[sabado], [domingo]:")

print(f"o sabor escolhido da pizza é {pizza_sabor}, o tamanho é {pizza_tamanh0} e hoje é {dia_semana}.")
# promoções -> estruturas condicionais
#comprando qualquer pizza e qualquer tamanho no sabado, o refri é gratuito
# comprando uma pizza de calabresa tamanho medio, em qualquer dia, o frete é gratuito
# comprando quaklquer pizza de qualquer tamanho no domingo, o frete e o refri são gratuitos.