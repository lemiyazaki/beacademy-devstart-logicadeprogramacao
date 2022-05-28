# Lógica de Programação - exercício 19
#  Programa que permita ao usuário escolher a operação a realizar. Em seguida solicite os dados para concretizar a operação e imprima o nome da operação feita e os dados referentes a ela
saldo = 1000
repetir = "s"
while repetir=="s":
  operacao=input("Selecione a operação a ser realizada:\nDigite:\ns para saque\nd para depósito\nt para transferência\ne para empréstimo\n")
  valor=float(input("Digite o valor da operação:"))
  banco = input("Digite o nome do Banco: ")
  agencia = input("Digite o número da Agência: ")
  conta = input("Digite o número da conta: ")
  match operacao:
    case "s":
      print("Saque selecionado")
      print("Saldo inicial:", saldo)
      saldo = saldo - valor
      print("Saldo atual:", saldo)
      print("O saque de R$", valor, "foi realizado no banco", banco, "agência", agencia, "conta", conta)
    case "d":
      print("Depósito selecionado")
      print("Saldo inicial:", saldo)
      saldo = saldo + valor
      print("Saldo atual:", saldo)
      print("O depósito de R$", valor, "foi realizado no banco", banco, "agência", agencia, "conta", conta)
    case "t":
      print("Transferência selecionada")
      print("Saldo inicial:", saldo)
      saldo = saldo - valor
      print("Saldo atual:", saldo)
      print("A transferência de R$", valor, "foi realizada para o banco", banco, "agência", agencia, "conta", conta)
    case "e":
      print("Empréstimo selecionado")
      print("Saldo inicial:", saldo)
      saldo = saldo + valor
      print("Saldo atual:", saldo)
      print("O empréstimo de R$", valor, "foi realizado no banco", banco, "agência", agencia, "conta", conta)
  repetir=input("Digite s para realizar outra operação\n")