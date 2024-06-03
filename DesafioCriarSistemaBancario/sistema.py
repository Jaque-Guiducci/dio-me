menu = """ 
[d] Depositar
[s] Sacar 
[e] Extrato 
[q] Sair 
    
Digite a opção desejada =>  """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Valor inválido! Informe um valor maior que zero.")
            
    elif opcao == "s":
        valor = float(input("Informe o valor de saque desejado:"))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Falha na Operação: Saldo insuficiente!")
            print(f"\nSeu saldo é: R$ {saldo:.2f}")
        
        elif excedeu_limite:
            print("Falha na Operação: O valor informado excedeu o limite permitido!")
                    
        elif excedeu_saque:
            print("Falha na Operação: Número máximo de saques excedido!")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
        else:
            print("Falha na Operação: Digite um valor maior que zero!")
        
    elif opcao == "e":
        print("\n##################### EXTRATO ######################")
        print("Nenhuma movimentação realizada." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("######################################################")

    elif opcao == "q":
        print("Obrigada por utilizar nossos serviços!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")