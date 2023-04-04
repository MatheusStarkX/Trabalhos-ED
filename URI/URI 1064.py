#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

vetor = []
contador = 0
soma = 0
for x in range(6):
	vetor.append(float(input()))
for numero in vetor:
	if numero > 0:
		contador = contador+1
		soma = soma+numero

media = soma/contador
print(f'{contador} valores positivos') 
print(f'{media:.1f}')
