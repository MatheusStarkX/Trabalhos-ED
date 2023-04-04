#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

x = 0
y = 1

while x != y:
	num = input().split()
	x = int(num[0])
	y = int(num[1])

	if x < y:
		print('Crescente')
	if x > y:
		print('Decrescente')
	