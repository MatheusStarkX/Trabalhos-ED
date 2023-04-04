#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

x = int(input())
y = int(input())

soma = 0
if x<y:
	z=x
	x=y
	y=z
	
for num in range(y+1,x):
	if num%2 != 0:
		soma = soma+num

print(soma)
