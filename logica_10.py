# Lógica de Programação - exercício 10
# Programa que receba do usuário a figura geométrica que deseja calcular a área e o perímetro (Q-Quadrado ou T-Triângulo) e calcule e exiba a área e o perímetro da figura escolhida
# Considerando formas equilaterais
forma = input("Digite a forma geométrica que deseja:\nq para quadrado\nt para triângulo\n")
lado = float(input("Digite o comprimento do lado: "))
match forma:
  case "t":
    area = (sqrt(3)/4)*(lado**2)
    perimetro = lado*3
  case "q":
    area = lado**2
    perimetro = lado*4
print("Área:", area)
print("Perímetro:", perimetro)