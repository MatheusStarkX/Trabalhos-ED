#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

x, y, z = input().split()
x = float(x)
y = float(y)
z = float(z)

if x >= y and x >= z:
	n1 = x
	if y >= z:
		n2 = y
		n3 = z
	else:
		n2 = z
		n3 = y
if x >= y and x <= z:
	n1 = z
	n2 = x
	n3 = y
if x <= y and x >= z:
	n1 = y
	n2 = x
	n3 = z
if x <= y and x <= z:
	n3 = x
	if z >= y:
		n1 = z
		n2 = y
	else:
		n1 = y
		n2 = z

if n1 >= n2+n3:
	print('NAO FORMA TRIANGULO')
else:
  if n1**2 == n2**2 + n3**2:
    print('TRIANGULO RETANGULO')
  if n1**2 > n2**2 + n3**2:
    print('TRIANGULO OBTUSANGULO')
  if n1**2 < n2**2 + n3**2:
    print('TRIANGULO ACUTANGULO')
  if n1 == n2 and n1 == n3:
    print('TRIANGULO EQUILATERO')
  if (n1 == n2 and n1 != n3) or (n2 == n3 and n2 != n1):
    print('TRIANGULO ISOSCELES')