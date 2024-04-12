menu = """
[d] Depositar [s] Sacar [e] Extrato [q] Sair
=> """

MSG_SUCESSO = {"deposito" : "Depósito realizado com sucesso!", "saque" :"Saque realizado com sucesso!"}

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

def programa():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

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

        elif opcao == "q":
            break

        else:
            exibir_mensagem("Operação inválida, por favor selecione novamente a operação desejada.")


programa()