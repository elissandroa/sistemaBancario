from copy import deepcopy
import os
from datetime import datetime

menu = """

         Sistema Bancário 1.0
                
                (1) - Depositar
                (2) - Sacar
                (3) - Visualizar extrato
                (4) - Nova conta
                (5) - Listar contas
                (6) - Novo cliente
                (7) - Listar clientes
                (8) - Sair          
                
                
                
                
"""

saques = []
clientes = []
clientes_aux = []
depositos = []
contas = []
extratos = []
option = 0
AGENCIA = "0001"
SAQUES_PERMITIDOS = 3
SAQUE_MAXIMO = 500.00


def cadastrar_cliente():
   cpf = input("Digite o CPF:")
   if not clientes:
      adiciona_cliente(cpf)
      print("Cliente adicionado !")
      input("Tecle enter para continuar ...")
     
   else:     
      for cliente in clientes:
           if cpf in cliente["cpf"] :
                print("Cpf já Cadastrado !")
                input("Tecle enter para continuar ...")
                break
           else:
                print("Lista com dados")
                adiciona_cliente(cpf)
                print("Cliente Adicionado")
                input("Tecle enter para continuar ...") 
                break


def adiciona_cliente(cpf):
     nome = input("Digite o nome do cliente: ")
     data_nascimento = input("Digite a data de nascimento: ")
     print("Digite o endereço: ")
     logradouro = input("Logradouro: ")
     bairro = input("Bairro:")
     cidade = input("Cidade:")
     estado = input("Sigla do estado:")
     clientes.append(
                {"nome":nome,
                "data_nascimento":data_nascimento,
                "cpf": cpf,
                "logradouro":logradouro,
                "bairro":bairro,
                "cidade":cidade,
                "estado":estado
                 })

def listar_clientes():
    if not clientes:
        print("Não há clientes cadastrados !")
        input("Tecle enter para continuar ...")
    else:    
        for cliente in clientes:
            print(cliente)
            input("Tecle enter para continuar ...")

def depositar(deposito, numero_conta, /):
    if not contas:
        print("Nenhuma conta cadastrada no sistema\nCadastre o cliente!")
        input("Tecle enter para continuar ...")
    else:    
        numero_conta = int(numero_conta)
        deposito = float(deposito)
        for conta in contas:
            if numero_conta == conta['Conta']:
                conta['Saldo'] += deposito
                extratos.append({"Conta":numero_conta, "valor": deposito})
                print("Depósito efetuado com sucesso !")
                input("Tecle enter para continuar ...")
                break
            else:
                print("Conta não cadastrada !")
                input("Tecle enter para continuar ...")

def verifica_numero_saques(conta):
    cont = 0
    for saque in saques:
        if saque['Conta'] == conta:
            cont += 1
    return cont     


def sacar(*, saque, numero_conta):
    if not contas:
        print("Nenhuma conta cadastrada no sistema\nCadastre o cliente!")
        input("Tecle enter para continuar ...")
    else:  
        numero_conta = int(numero_conta)
        saque = float(saque)
        if verifica_numero_saques(numero_conta) < SAQUES_PERMITIDOS:
            if saque <= 500:    
                for conta in contas:
                    if numero_conta == conta['Conta']:
                        if saque <= conta['Saldo']:
                           conta['Saldo'] -= saque
                           extratos.append({"Conta":numero_conta, "valor": -(saque)})
                           saques.append({"Conta":numero_conta})
                           print("Saque efetuado com sucesso ...")
                           input("Tecle enter para continuar ...")
                        else:            
                           print("Saldo insuficiente !")
                           input("Tecle enter para continuar ...")
            else:
                print("Valor máximo de saque excedido!")
                input("Tecle enter para continuar ...")
        else:
            print("Número de saques excedido!")
            input("Tecle enter para continuar ...")

def criar_conta():
    print("Cadastro de conta corrente")
    cpf = input("Digite o cpf do cliente: ")
    cliente_aux = deepcopy(clientes)

    for index, cliente in enumerate(cliente_aux):
        if cpf in cliente["cpf"]:
            cod = len(contas)
            contas.append({"Codigo":index,"Agencia": AGENCIA,"Conta":cod+1,"Usuario": cliente, "Saldo": 0.0 })
            print(f"Conta criada com sucesso para {retorna_cliente(cod+1)}! ") 
            input("Tecle enter para continuar ...")
            break
            
    else:
       print("Cliente não cadastrado! Faça o cadastro primeiro")
       input("Tecle enter para continuar ...")
     

def listar_contas():
    if not contas:
        print("Não há contas para exibir !")
        input("Tecle enter para continuar ...")
    else:    
        for conta in contas:
             print(conta)
    input("Tecle enter para continuar ...")            


def retorna_cliente(conta):
    for cont in contas:
        if cont['Conta'] == conta:
           return cont['Usuario']['nome']


def imprimir_extrato(conta, /, * , data):
    if not extratos:
        print("Sem dados para exibir!")
        input("Tecle enter para continuar ...")
    else:    
        print("""


        """)
        print("Extrado Sistema bancário 1.0")
        print(f"Cliente: {retorna_cliente(conta)}")
        print("Data:",data)
        print(f"Conta: {conta}")
        for extrato in extratos:
            if extrato['Conta'] == conta:
                if extrato['valor'] > 0:
                    print(f"depósito: R$  {extrato['valor']:18.2f}")
                else:
                    print(f"saque:    R$  {extrato['valor']:18.2f}")
        for cont in contas:
            if conta == cont['Conta']:
                print("*"*32)
                print(f"Saldo :   R$ {cont['Saldo']:19.2f}")
                print("*"*32)
                break
        input("Tecle enter para continuar ...")        

def data_transacao():
    data = datetime.now()
    return data.strftime('%d/%m/%Y')

def limpa_tela():
    os.system('cls') or None

limpa_tela()
print(menu)
while option != 8:
    option = int(input())
    if option == 1:
        print("Operação de depósito")
        deposito = float(input("Valor do depósito: "))
        numero_conta = int(input("Digite o número da conta: "))
        depositar(deposito, numero_conta)
        limpa_tela()
        print(menu)
    elif option == 2:
        print("Operação de saque")
        saque = float(input("Valor do saque: "))
        conta = int(input("Digite o número da conta: "))
        sacar(saque = saque, numero_conta=conta)
        limpa_tela()
        print(menu)
    elif option == 3:
        print("Obter extrato")
        conta = int(input("Número da conta: "))
        data = data_transacao()
        imprimir_extrato(conta, data=data)
        limpa_tela()
        print(menu)
    elif option == 4:
        criar_conta()
        limpa_tela()
        print(menu)
    elif option == 5:
        listar_contas()
        limpa_tela()
        print(menu)
    elif option == 6:
        print("Cadastro de cliente")
        cadastrar_cliente()
        limpa_tela()
        print(menu)
    elif option == 7:
        listar_clientes()
        limpa_tela()
        print(menu)
    elif option == 8:
        print("Saindo ...")
    else:
        print("Valor inválido")
        input("Tecle enter para continuar ...")
        limpa_tela()
        print(menu)
        
      
