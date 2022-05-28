# Lógica de Programação - exercício 27
# Programa que permita o cadastro de uma Matriz e exiba a soma da diagonal principal e secundária
tamanho = int(input("Digite o tamanho da matriz quadrada: "))
matriz = []
soma_pri = 0
soma_sec = 0
for i in range(tamanho):
  coluna = []
  for j in range(tamanho):
    valor = int(input(f"Digite o número da linha {i+1} coluna {j+1}: "))
    coluna.append(valor)
  matriz.append(coluna)
for i in range(tamanho):
  for j in range(tamanho):
    if i==j:
      soma_pri = soma_pri+matriz[i][j]
    if i+j==tamanho-1:
      soma_sec = soma_sec+matriz[i][j]
print("Soma da diagonal principal:", soma_pri)
print("Soma da diagonal secundária:", soma_sec)