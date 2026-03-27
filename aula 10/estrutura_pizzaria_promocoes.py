#variaveia da pizzaria 
FRETE= 2 #constante fake em python
pizza_sabor= input("informe o sabor da pizza - [frango com requeijão], [calabresa], [mussarela], [banana com chocolate]:")
pizza_tamanh0= input("informe o tamanho da pizza - [pequena], [medio], [grande]:")
dia_semana= input("informe o dia da semana - [quarta], [quinta], [sexta] ,[sabado], [domingo]:")

print(f"o sabor escolhido da pizza é {pizza_sabor}, o tamanho é {pizza_tamanh0} e hoje é {dia_semana}.")
# promoções -> estruturas condicionais
#comprando qualquer pizza e qualquer tamanho no sabado, o refri é gratuito
if dia_semana == "sabado" :
    print(f"🍕 pedido aceito com sucesso!")
    print(f" 🥤o refri hoje é por conta da casa.")
elif dia_semana == "domingo" :
    print(f"🍕 pedido aceito com sucesso!")
    print(f" o frete e🥤o refri hoje é por conta da casa.")
    
elif pizza_sabor == "calabresa" and pizza_tamanh0 == "media":
    print(f"🍕 pedido aceito com sucesso!")
    print(f" o frete e🥤o refri hoje é por conta da casa.")

# comprando uma pizza de calabresa tamanho medio, em qualquer dia, o frete é gratuito

# comprando quaklquer pizza de qualquer tamanho no domingo, o frete e o refri são gratuitos.
