# Lógica de Programação - exercício 14
# Programa que imprima os múltiplos de 3 entre dois números digitados pelo usuário
valor1 = int(input("Digite um número inicial: "))
valor2 = int(input("Digite um número final: "))
for i in range(valor1, valor2+1):
  if i%3==0:
    print(i)