# crie um sistema aonde o valor inicial é de R$1000 reais e o usuario consiga realizar o saque e ao final seja exibido o valor restante do saldo 
saldo= 1000
while saldo > 0: 
    saque = float(input("digite o valor do saque: "))
    saldo -= saque # saldo = saldo - saque 
    print (f'saldo restante: {saldo}')
