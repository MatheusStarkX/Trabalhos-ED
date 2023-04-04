#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

vetor = []
contador = 0
for x in range(5):
	vetor.append(int(input()))
for numero in vetor:
	if numero%2 == 0:
		contador = contador+1

print(f'{contador} valores pares') 