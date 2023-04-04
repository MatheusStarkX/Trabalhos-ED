#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

n = int(input())
media = []
for k in range(n):
	testes = input().split()
	x = float(testes[0])
	y = float(testes[1])
	z = float(testes[2])
	media.append((2*x + 3*y + 5*z)/10)
for num in media:
  print(f'{num:.1f}')