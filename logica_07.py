# Lógica de Programação - exercício 07
# Programa que recebe a idade da pessoa e a classifique de acordo com a tabela
idade = int(input("Digite a idade: "))
if idade < 18:
  print("Menor de idade")
elif 18<=idade<60:
  print("Adulto")
else:
  print("Idoso")