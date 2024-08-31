saldo = 0.0
extrato = []
limite_saque_diario = 3
saques_realizados = 0
limite_saque_valor = 500.0


def depositar():
    global saldo, extrato
    valor = float(input("Digite o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Deposito: R$ {valor:.2f}")
        print(f"Deposito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("valor do deposito inválido. Tente novamente.")


def sacar():
    global saldo, extrato, saques_realizados
    if saques_realizados >= limite_saque_diario:
        print("Limite diário de saques atingido.")
        return
    valor = float(input("Digite o valor do saque: "))
    if valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite_saque_valor:
        print("O valor excede o limite de saque permitido por transação.")
    else:
        saldo -= valor
        saques_realizados += 1
        extrato.append(f"Saque: R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")


def visualizar_extrato():
    global saldo, extrato
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for item in extrato:
            print(item)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")


while True:
    print("\nEscolha uma operação:")
    print("d - Depositar")
    print("s - Sacar")
    print("e - Visualizar Extrato")
    print("q - Sair")
    
    opcao = input("Digite a opção desejada: ")
    
    if opcao == "d":
        depositar()
    elif opcao == "s":
        sacar()
    elif opcao == "e":
        visualizar_extrato()
    elif opcao == "q":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")