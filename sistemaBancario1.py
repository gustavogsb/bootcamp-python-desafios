menu = f"""
 ---Transações------------Usuário----------------Conta----------------
                |                           |
 [d] Depositar  |  [u] Cadastrar Usuário    |  [c] Cadastrar Conta
 [s] Sacar      |  [lu] Listar Usuários     |  [lc] Listar Contas 
 [e] Extrato    |                           |
 ---------------------------------------------------------------------
 [q] Sair
 ---------------------------------------------------------------------
=> """

MSG_SUCESSO = {"deposito" : "Depósito realizado com sucesso!", 
               "saque" :"Saque realizado com sucesso!",
               "usuario":"Usuário criado com sucesso!",
               "conta":"Conta criada com sucesso!"}

AGENCIA = "0001"

def exibir_mensagem(msg):
    print(msg)

def depositar(valor, saldo, extrato, /):
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    print(MSG_SUCESSO["deposito" ])
    return saldo, extrato

def sacar(*, saldo, valor, numero_saques, limite_saques, extrato):

    if numero_saques >= limite_saques:
        exibir_mensagem("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque: R$ {valor:.2f}\n" 
        print(MSG_SUCESSO["saque" ])      

    return saldo, numero_saques, extrato

def verificar_saldo(valor, saldo):
    return valor > saldo

def verificar_limite(valor, limite_conta):
    return valor > limite_conta

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (sem máscara): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        exibir_mensagem("\n Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(MSG_SUCESSO["usuario"])  

    return usuarios
      

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_usuarios(usuarios):
    if(len(usuarios) > 0):
        for usuario in usuarios:
            conteudo = f"""\
                CPF:\t{usuario['cpf']}
                Nome:\t{usuario['nome']}
                Data de Nascimento:\t{usuario['data_nascimento']}
                Endereço:\t{usuario['endereco']}
            """
            exibir_mensagem("=" * 100)
            exibir_mensagem(conteudo)
            exibir_mensagem("=" * 100)
    else:
       exibir_mensagem("\n Não existe usuários cadastrados") 


def cadastrar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        exibir_mensagem("\n Conta criada com sucesso! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    exibir_mensagem("\n Usuário não encontrado !")


def listar_contas(contas):
    if(len(contas) > 0):
        for conta in contas:
            conteudo = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            """
            exibir_mensagem("=" * 100)
            exibir_mensagem(conteudo)  
            exibir_mensagem("=" * 100)     
    else:
       exibir_mensagem("\n Não existe contas cadastradas") 

def programa():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    usuarios = []
    contas = []    

    while True:

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo, extrato = depositar(valor, saldo, extrato)
            else:
                exibir_mensagem("Operação falhou! O valor informado é inválido.")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            if verificar_saldo(valor, saldo):
                exibir_mensagem("Operação falhou! Você não tem saldo suficiente.")

            elif verificar_limite(valor, limite):
                exibir_mensagem("Operação falhou! O valor do saque excede o limite.")

            elif valor > 0:
                saldo, numero_saques, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
                    extrato=extrato
                )
            else:
                exibir_mensagem("Operação falhou! O valor informado é inválido.")

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            usuarios = cadastrar_usuario(usuarios)   

        elif opcao == "lu":
            listar_usuarios(usuarios)    

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)                 

        elif opcao == "q":
            break

        else:
            exibir_mensagem("Operação inválida, por favor selecione novamente a operação desejada.")


programa()