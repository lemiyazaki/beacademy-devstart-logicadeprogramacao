# Lógica de Programação - exercício 23
# Crie um programa inicie o saldo do cliente com R$1000,00 e que permita o saques consecutivos no valor de R$ 150.00 até que seu saldo seja negativo
saldo = 1000
while saldo > 0:
  saque=input("Digite s para realizar um saque de R$150\n")
  if saque == "s":
    saldo = saldo - 150
print("Saldo insuficiente para realizar a operação")