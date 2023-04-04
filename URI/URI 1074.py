#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

n = int(input())
vetor = []
for k in range(n):
  vetor.append(int(input()))
for num in vetor:
	if num%2 != 0 and num > 0:
		print('ODD POSITIVE')
	if num%2 != 0 and num < 0:
		print('ODD NEGATIVE')
	if num%2 == 0 and num > 0:
		print('EVEN POSITIVE')
	if num%2 == 0 and num < 0:
		print('EVEN NEGATIVE')
	if num == 0:
		print('NULL')