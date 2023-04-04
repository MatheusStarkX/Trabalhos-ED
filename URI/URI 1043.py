#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

x, y, z = input().split()
x = float(x)
y = float(y)
z = float(z)

if (y-z) < x < (y+z) and (x-z) < y < (x+z) and (x-y) < z < (x+y):
	soma = x+y+z
	print(f'Perimetro = {soma:.1f}')
else:
	area = ((x+y)*z)/2
	print(f'Area = {area:.1f}')


