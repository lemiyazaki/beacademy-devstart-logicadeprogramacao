# Lógica de Programação - exercício 11
# Programa que permita ao usuário escolher a operação a realizar (depósito ou saque ou transferência) , caso a operação seja de transferência solicite o nome do banco, da agência e conta, receba as informações e, ao final exiba o valor inicial, a operação realizada e o saldo atual, no caso de transferência exiba também os dados do banco, agência e conta
saldo = 1000
operacao=input("Selecione a operação a ser realizada:\nDigite:\ns para saque\nd para depósito\nt para transferência\n")
valor=float(input("Digite o valor da operação:"))
match operacao:
  case "s":
    print("Saque selecionado")
    print("Saldo inicial:", saldo)
    saldo = saldo - valor
    print("Saldo atual:", saldo)
  case "d":
    print("Depósito selecionado")
    print("Saldo inicial:", saldo)
    saldo = saldo + valor
    print("Saldo atual:", saldo)
  case "t":
    print("Transferência selecionada")
    banco = input("Digite o nome do Banco: ")
    agencia = input("Digite o número da Agência: ")
    conta = input("Digite o número da conta: ")
    print("Saldo inicial:", saldo)
    saldo = saldo - valor
    print("Saldo atual:", saldo)
    print("A transferência foi realizada para o banco", banco, "agência", agencia, "conta", conta)
