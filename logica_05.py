# Lógica de Programação - exercício 05
# Programa que recebe um valor de depósito do usuário e atualiza o seu saldo. Ao final exibe o valor inicial o depósito e o saldo atual.
saldo = float(input("Digite o valor do saldo: "))
deposito = float(input("Digite o valor do depósito: "))
print("Saldo inicial:", saldo)
print("Valor depositado:", deposito)
print("Salto atual:", saldo+deposito)