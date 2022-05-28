# Lógica de Programação - exercício 26
# Programa que permita ao usuário cadastrar dados de 5 clientes, guarda os dados em um vetor e ao final os exibe
nome = []
cpf = []
rg = []
endereco = []
telefone = []
for i in range(5):
  entrada = input(f"Digite o nome do cliente {i+1}: ")
  nome.append(entrada)
  entrada = input(f"Digite o cpf do cliente {i+1}: ")
  cpf.append(entrada)
  entrada = input(f"Digite o rg do cliente {i+1}: ")
  rg.append(entrada)
  entrada = input(f"Digite o endereço do cliente {i+1}: ")
  endereco.append(entrada)
  entrada = input(f"Digite o telefone do cliente {i+1}: ")
  telefone.append(entrada)
for i in range(5):
  print("\nCliente", i+1)
  print("Nome:", nome[i])
  print("CPF:", cpf[i])
  print("RG:", rg[i])
  print("Endereço:", endereco[i])
  print("Telefone:", telefone[i])