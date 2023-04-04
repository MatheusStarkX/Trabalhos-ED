#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

i = 1

while i != 2:
	coord = input().split()
	x = int(coord[0])
	y = int(coord[1])

	if x == 0 or y == 0:
		break
	if x > 0 and y > 0:
		print('primeiro')
	if x < 0 and y > 0:
		print('segundo')
	if x < 0 and y < 0:
		print('terceiro')
	if x > 0 and y < 0:
		print('quarto')