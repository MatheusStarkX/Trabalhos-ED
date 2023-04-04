#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

x , y = input().split()

x = float(x)  
y = float(y)

if x == 0 and y == 0:
	print("Origem")
if x == 0 and y != 0:
	print("Eixo Y")
if x != 0 and y == 0:
	print("Eixo X")
if x > 0 and y > 0:
	print("Q1")
if x < 0 and y > 0:
	print("Q2")
if x < 0 and y < 0:
	print("Q3")
if x > 0 and y < 0:
	print("Q4")