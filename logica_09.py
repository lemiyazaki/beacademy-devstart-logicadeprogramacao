# Lógica de Programação - exercício 09
# Programa que solicite ao usuário a operação desejada e implemente as quatro operações matemáticas
operacao = input("Digite a operação que deseja realizar:\n+ para soma\n- para subtração\n* para multiplicação\n/ para divisão")
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
match operacao:
  case "+":
    resultado = valor1+valor2
  case "-":
    resultado = valor1-valor2
  case "*":
    resultado = valor1*valor2
  case "/":
    resultado = valor1/valor2
print("O resultado da operação é", resultado)