# Desafio: criar um sistemas bancários
##Deve possuir as funções sacar, depositar e visualizar extrato.

menu = '''
============== Bem-vindo =================
Escolha a ação que deseja fazer na sua conta:

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=========================================

'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print(f'''
A opção selecionada foi Depósito!
O seu saldo atual é: R${saldo:.2f}\n !            
             ''')

        deposito = float(input("digite o valor que você deseja depositar:  "))
    
        if deposito <= 0:
            print("Valores nulos ou negativos não são aceitos.")
        else:
            saldo += deposito
            extrato += f"Depósito: R${deposito:.2f}\n"
            
            print(f'''
Seu depósito de R${deposito} foi efetuado!
Seu atual saldo é de:
R${saldo}
''')

    elif opcao == "s":
        print(f'''
A opção selecionada foi Saque!
O seu saldo atual é: R${saldo:.2f}\n              
O seu limite de saques é de R${limite}              
Você possui {LIMITE_SAQUES} restantes para hoje!            
              ''')
        
        saque = float(input("Digite o valor que você deseja retirar:  "))
        
        if saque > 500:
            print("Saque recusado, acima do limite de R$500")
        elif LIMITE_SAQUES == 0:
            print("limite de saque diarios atingido, tente novamente amanhã.")
        elif saque <= 0:
            print("saque recusado, valores nulos e negativos não são aceitos")
        elif saldo == 0:
            print("Saque recusado, saldo nulo")
        elif saldo < saque:
            print("saque recusado, saldo insuficiente")
        else:
            saldo -= saque
            extrato += f"Saque: R${saque:.2f}\n"
            numero_saques += 1
            LIMITE_SAQUES -= 1

            print(f'''
Foi sacado R${saque} da sua conta.
Seu saldo atual é de R${saldo}
Você possui {LIMITE_SAQUES} restantes para hoje.
''')

    elif opcao =="e":
        print("\n================ EXTRATO =================")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")

    elif opcao == "q":
        break

    else:
        print('''

A opção selecionada não foi reconhecida

Cheque a opção selecionada novamente

Caso acredite que houve um erro contate a assitência

              ''')