# Lógica de Programação - exercício 21
# Solicitar a idade de várias pessoas e imprimir:
# • Total de pessoas com menos de 18 anos.
# • Total de pessoas com mais de 60 anos.
# • O programa termina quando idade for =-99
total_menor=0
total_maior=0
idade=None
while idade!=-99:
  idade=int(input("Digite a idade: "))
  if idade<18 and idade!=-99:
    total_menor=total_menor+1
  elif idade>60:
    total_maior=total_maior+1
print("Total de pessoas com menos de 18 anos:", total_menor)
print("Total de pessoas com mais de 60 anos:", total_maior)