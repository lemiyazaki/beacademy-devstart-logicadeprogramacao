# Lógica de Programação - exercício 03
# Programa que declare 3 variáveis para receber o Nome, o peso e a altura de uma pessoa. Ao final imprima os dados na tela, calcule e exiba o IMC
nome = input("Digite o nome: ")
peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))
print("Nome:", nome)
print("Altura:", altura, "m")
print("Peso:", peso, "kg")
# Cálculo IMC = peso/(altura*altura)
print("IMC:",(peso/(altura**2)))