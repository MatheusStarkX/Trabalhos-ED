#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

vetor = []
contpar = 0
contimpar = 0
contposi = 0
contnega = 0

for x in range(5):
	vetor.append(int(input()))
for numero in vetor:
	if numero > 0:
		contposi = contposi+1
	if numero < 0:
		contnega = contnega+1
	if numero%2 == 0:
		contpar = contpar+1
	else:
		contimpar = contimpar+1

print(f'{contpar} valor(es) par(es)') 
print(f'{contimpar} valor(es) impar(es)') 
print(f'{contposi} valor(es) positivo(s)') 
print(f'{contnega} valor(es) negativo(s)') 
