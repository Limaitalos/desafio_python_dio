menu = """
  [d] Depositar
  [s] Sacar
  [e] Extrato
  [q] Sair
"""

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
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        # Verifica se o valor é positivo, se há saldo suficiente e se o número de saques permitidos não foi atingido
        if valor > 0:
            if valor <= saldo and numero_saques < LIMITE_SAQUES and valor <= limite:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            elif valor > saldo:
                print("Você não tem saldo suficiente para realizar o saque.")
            elif numero_saques >= LIMITE_SAQUES:
                print("Número máximo de saques diários atingido.")
            elif valor > limite:
                print(f"O valor do saque excede o limite permitido de R$ {limite:.2f}.")
        else:
            print("Valor inválido para saque.")

    elif opcao == "e":
        print("\n===== EXTRATO =====")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("===================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
