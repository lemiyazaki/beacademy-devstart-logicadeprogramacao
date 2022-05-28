# Lógica de Programação - exercício 16
# Programa que receba do usuário um número e apresente a Tabuada
numero = int(input("Digite um número: "))
i = 0
while i<=10:
  print(numero, "x", i, "=", numero*i)
  i=i+1