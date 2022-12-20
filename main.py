menu = """
                Sistema Bancário 1.0
                
                (1) - Depositar
                (2) - Sacar
                (3) - Visualizar extrato
                (4) - Sair
"""



saques = []
clientes = []
depositos = []







deposito = 0.0
saldo_deposito = 0.0
saldo_saque = 0.0
saldo = 2000
saque = 0.0
limite_saque = 500.00

def isfloat(num):
    return num.replace('.','').isdigit()


option = " "
msg = ""
print(menu)


option = int(input())
while option != 4:
    if option == 1:
        deposito = input("Digite o valor que deseja depositar: ")
        if isfloat(deposito) and deposito.isnumeric:
            deposito = float(deposito)
            if deposito > 0:    
                depositos.append(deposito)
                saldo += deposito
                print("Deposito efetuado com sucesso")
                saldo_deposito += deposito
                print(f'Saldo: R${saldo:.2f}')
                input("Pressione enter para continuar ...")
                print(menu)
                option = int(input())
            else:
                print("Valor de depósito precisa ser maior que 0")
                input("Pressione enter para continuar ...")
                print(menu)
                option = int(input())    
        else:
            print("Somente são aceitos números positivos neste campo!")

    elif option == 2:
        if len(saques) <= 2:
            saque = input("Digite o valor que deseja sacar: ")
            if isfloat(saque) and saque.isnumeric:
                saque = float(saque)
                if saldo < saque:
                    print("Saldo insuficiente! ")
                    continue
                    input("Pressione enter para continuar ...")
                    print(menu)
                    option = int(input())
                if saque > 500:
                        print("Valor permitido de saque exedido!")
                        input("Pressione enter para continuar ...")
                        print(menu)
                        option = int(input())
                if  saldo > saque and 0 < saque <= 500:
                    saldo -= saque
                    saques.append(saque)
                    saldo_saque += saque
                    print("Qtd saques:",len(saques))
                    print(f'Saldo: R${saldo:.2f}')
                    print("Aguarde a saída do seu dinheiro...")
                    print("Saque efetuado com sucesso ...")
                    input("Pressione enter para continuar ...")
                    print(menu)
                    option = int(input())
            else:
                print("Somente são aceitos números neste campo!")    

        else:
            print("Limite de saques excedido !")
            input("Pressione enter para continuar ...")
            print(menu)
            option = int(input())
    
    elif option == 3:
        print(" Extrato bancário ".center(64, "*"))
        print(f"SALDO: R${(saldo - saldo_deposito + saldo_saque):14.2f}")
        print(" Depósitos ".center(64, "*"))
        if len(depositos) == 0:
            print("Sem depósitos hoje !")    
        else:
            for deposito in depositos:
                print(f"deposito: R$ {deposito:10.2f}")
        print(" Saque ".center(64, "*"))
        if len(saques) == 0:
            print("Sem saques hoje!")  
        else:      
            for saque in saques:
                print(f"saque: R${saque:14.2f}") 
        print("*".center(64, "*"))
        print(f"SALDO: R${saldo:.2f}")
        input("Pressione enter para continuar ...")
        print(menu)
        option = int(input())  
        


    elif option == 4:
        print("Saindo ...")
    else:
        print("Opção inválida !")
