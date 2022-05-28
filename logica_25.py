# Lógica de Programação - exercício 25
# Programa que permita cadastrar os seguintes dados de um Aluno: Nome, nota1 e nota2. Receba estes valores em vetores e calcule e exiba ao final todos os dados e a informação se o aluno foi aprovado(media maior ou igual a 6) ou reprovado(media inferior a 6)
notas = []
for i in range(2):
  parcial = float(input(f"Digite a nota {i+1}\n"))
  notas.append(parcial)
for i in range(2):
  total = notas[i]
  print("Nota", i+1, ":", notas[i])
media = (notas[0]+notas[1])/2
print("Média:", media)
if media >= 6:
  print("Aprovado")
else:
  print("Reprovado")