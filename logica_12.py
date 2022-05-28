# Lógica de Programação - exercício 12
# Programa que receba do usuário um número e apresente a Tabuada
numero = int(input("Digite um número: "))
for i in range(11):
  print(numero, "x", i, "=", numero*i)