#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)

if x > y and x > z:
	n1 = x
	if y > z:
		n2 = y
		n3 = z
	else:
		n2 = z
		n3 = y
if x > y and x < z:
	n1 = z
	n2 = x
	n3 = y
if x < y and x > z:
	n1 = y
	n2 = x
	n3 = z
if x < y and x < z:
	n3 = x
	if z > y:
		n1 = z
		n2 = y
	else:
		n1 = y
		n2 = z

print(f'{n3}\n{n2}\n{n1}') 
print()
print(f'{x}\n{y}\n{z}')