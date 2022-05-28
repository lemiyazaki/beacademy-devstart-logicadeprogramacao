# Lógica de Programação - exercício 24
# Programa que solicite ao usuário o nome e o preço de 10 produtos e armazene-os em um vetor. Ao final imprima o nome e os valores correspondentes dos produtos
nome = []
preco = []
for i in range(10):
  nome_prod=input(f"Digite o nome do {i+1}º produto\n")
  nome.append(nome_prod)
  preco_prod=input(f"Digite o preço do {i+1}º produto\n")
  preco.append(preco_prod)
for i in range(10):
  print("O preço de", nome[i], "é R$", preco[i])