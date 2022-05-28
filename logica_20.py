# Lógica de Programação - exercício 20
# Programa que permita ao usuário tentar logar em seu Sistema informando seu nome e senha. Repita a operação até que o nome e senha correspondam a um valor armazenado(Marcos – 1234). Caso o usuário digite -1 interrompa a repetição e informe que o programa será finalizado por solicitação do usuário
nome="nome"
senha="senha"
while nome!="Marcos" or senha!="1234":
  nome=input("Digite seu nome: ")
  senha=input("Digite a senha: ")
  if nome == "-1" or senha == "-1":
    print("Programa finalizado por solicitação do usuário")
    break