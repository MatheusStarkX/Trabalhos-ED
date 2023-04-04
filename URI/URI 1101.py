#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

x = 1
y = 2

while x > 0 and y > 0:
	soma = 0
	valores = []
	num = input().split()
	num.sort()
	x = int(num[0])
	y = int(num[1])
	if x <= 0:
		break
	
	while x <= y:
		soma += x
		valores.append(x)
		print(x, end=' ')
		x += 1

	print(f'Sum={soma}')