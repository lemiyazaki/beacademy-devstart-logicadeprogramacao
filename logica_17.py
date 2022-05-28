# Lógica de Programação - exercício 17
# Programa que solicite ao usuário o seu nome e senha do cartão e valide se a senha e nome são corretos (Nome: Marcos e senha: paylivre) e, caso positivo, dê boas vindas ao usuário e, em caso negativo, solicite os dados novamente
nome = "nome"
senha = "senha"
while nome!="Marcos" and senha!="paylivre":
  nome=input("Digite o nome: ")
  senha=input("Digite a senha: ")
print("Bem vindo!")