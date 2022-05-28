# Lógica de Programação - exercício 04
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
print("Nome:", nome)
print("Idade:", idade)
#Verdadeiro se idade é maior que 18
print("Idade maior que 18?", idade>18)
#Falso se idade é diferente de 25
print("Idade igual a 25?", idade==25)
#Falso se idade é diferente que 25 E nome é igual a Marcos
print("Idade igual a 25 OU nome diferente de Marcos?", idade==25 or nome!="Marcos")
#Verdadeiro se idade é diferente de 25 OU nome é igual a Marcos
print("Idade diferente de 25 OU nome igual a Marcos?", (idade!=25 or nome=="Marcos"))
#Verdadeiro de idade dividida por 2 é zero
print("Resto de idade dividida por 2 igual a zero?", idade%2==0)