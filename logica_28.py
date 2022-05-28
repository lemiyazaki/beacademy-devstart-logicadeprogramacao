# Lógica de Programação - exercício 28
# Pprograma que faça a leitura, a partir do teclado, dos valores numéricos das primeiras 4 linhas e 3 colunas da planilha. Realizada a leitura, armazenar a soma dos valores de cada linha na linha correspondente da última coluna. Finalmente, armazenar a soma dos valores de cada coluna na coluna correspondente da última linha da planilha. Imprima a planilha ao final
matriz = []
soma_col = [0,0,0,0]
for i in range(4):
  coluna = []
  soma_lin = 0
  for j in range(3):
    valor = int(input(f"Digite o número da linha {i+1} coluna {j+1}: "))
    coluna.append(valor)
    soma_lin = soma_lin + valor
    # soma_col[j] = soma_col[j] + valor
  coluna.append(soma_lin)
  matriz.append(coluna)
matriz.append(soma_col)

for i in range(4):
  for j in range(4):
    print(matriz[i][j], end=" ")
  print("")
