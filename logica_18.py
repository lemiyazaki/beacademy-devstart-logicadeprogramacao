# Lógica de Programação - exercício 18
# Programa que realize as 4 operações matemática a partir de dois números que serão digitados pelo usuário. Após isto imprima os valores na tela e em seguida pergunte se ele quer realizar novo cálculo, repetido as operações enquanto o usuário desejar continuar
repetir = "s"
while repetir == "s":
  valor1 = float(input("Digite o primeiro valor: "))
  valor2 = float(input("Digite o segundo valor: "))
  print(valor1, "+", valor2, "=", valor1+valor2)
  print(valor1, "-", valor2, "=", valor1-valor2)
  print(valor1, "*", valor2, "=", valor1*valor2)
  print(valor1, "/", valor2, "=", valor1/valor2)
  repetir=input("Digite s para realizar outra operação ou qualquer outra tecla para sair\n")