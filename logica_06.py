# Lógica de Programação - exercício 06
# Programa que recebe a altura e o peso da pessoa e a classifique de acordo com a tabela
peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))
imc = peso/(altura**2)
if imc<19:
  print("Abaixo do peso")
elif 19<=imc<25:
    print("Peso normal")
elif 25<=imc<30:
    print("Sobrepeso")
elif 30<=imc<40:
    print("Obesidade Tipo I")
elif imc>=40:
    print("Obesidade Mórbida")