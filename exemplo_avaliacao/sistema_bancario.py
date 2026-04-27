saldo = 1000.00
historico = [] # lista vazia

print (f'--- bem vindo ao caixa eletronico---')

while true: # imprime pelo menos o while uma vez
    print(f''' --- menu principal---
           [1] - depositar
           [2] - sacar
           [3] - ver saldo
           [4] - ver historico
           [5] - sair

        ''')
    opcao = input('➡️ escolha uma opção : ')
    
    # lógica para a opção de depósito 
    if opcao == '1' :
        valor_deposito = float (input('Digite o valor para Depósito: R$'))
        if valor_deposito > 0 :
           # saldo = saldo + valor_deposito
         saldo += valor_deposito
         registro = f'Deposito: +R$ {valor_deposito: . 2f}'
         historico. append(registro) # append() adiciona algo a lista 
         print('deposito realizado com sucesso.')
        else:
            print('valor invalido. O deposito deve ser um número positivo.')
    elif opcao == '2' :
        valor_saque = float(input('digite o valor para saque: R$'))
        if valor_saque <= 0:
           print('valor inválido! o saque deve ser um número positivo.')
        elif valor_saque > saldo:
            print('saldo insuficiente para realizar este saque.')
        else:
            # saldo = saldo - valor_deposito
            saldo -= valor_saque
            registro = f'Saque: -R$ {valor_saque:.2f}'
            historico.append(registro)
            print('saque realizado')
    elif opcao == '3':
        print(f'seu saldo é: R${saldo: .2f}')
    elif opcao == '4':
        print('---historico de transações---')
        if not historico: # verifica se historico está vazia, pois toda variavel/ estrutura vazia é true
            print('nenhuma transição foi realizada')
        else:
            for transacao in historico:
                print(transacao)
    elif opcao == '5':
        print('atendimento encerrado, bobão')
        break # encerra o laço while 
    else:
        print('sua anta, opção invalida, escolha uma das opções.') 
                  
                  
