menu = """
[d] Depositar [s] Sacar [e] Extrato [q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def exibir_mensagem(msg):
    print(msg)

def depositar(valor):
    global saldo
    saldo += valor

def sacar(valor):
    global saldo
    global numero_saques
    saldo -= valor
    numero_saques += 1

def verificar_saldo(valor):
    return valor > saldo

def verificar_limite(valor):
    return valor > limite

def verifcar_qtde_saque(numero_saques):
    return numero_saques >= LIMITE_SAQUES

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            depositar(valor)
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            exibir_mensagem("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if verifcar_qtde_saque(numero_saques):
            exibir_mensagem("Operação falhou! Número máximo de saques excedido.")
        
        elif verificar_saldo(valor):
            exibir_mensagem("Operação falhou! Você não tem saldo suficiente.")

        elif verificar_limite(valor):
            exibir_mensagem("Operação falhou! O valor do saque excede o limite.")

        elif valor > 0:
            sacar(valor)
            extrato += f"Saque: R$ {valor:.2f}\n"

        else:
            exibir_mensagem("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        exibir_mensagem("Operação inválida, por favor selecione novamente a operação desejada.")
