# Lógica de Programação - exercício 08
# Programa que permita ao usuário escolher a operação a realizar (depósito ou saque), receba a informação da operação escolhida e o valor do usuário e, em seguida, atualize o seu saldo. Ao final exiba o valor inicial, a operação realizada e o saldo atual
saldo = 1000
operacao=input("Selecione a operação a ser realizada:\nDigite:\ns para saque\nd para depósito\n")
valor=float(input("Digite o valor da operação:"))
if operacao=="s":
  print("Saque selecionado")
  print("Saldo inicial:", saldo)
  saldo=saldo-valor
  print("Saldo atual:", saldo)
elif operacao=="d":
  print("Saque selecionado")
  print("Saldo inicial:", saldo)
  saldo=saldo+valor
  print("Saldo atual:", saldo)
else:
  print("Operação inválida")
