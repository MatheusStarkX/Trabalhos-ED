#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

palavra = []
for x in range(3):
  palavra.append(input())

if palavra[0] == 'vertebrado':
	if palavra[1] == 'ave':
		if palavra[2] == 'carnivoro':
			animal = 'aguia'
		else:
			animal = 'pomba'
	else:
		if palavra[2] == 'onivoro':
			animal = 'homem'
		else:
			animal = 'vaca'
else:
	if palavra[1] == 'inseto':
		if palavra[2] == 'hematofago':
			animal = 'pulga'
		else:
			animal = 'lagarta'
	else:
		if palavra[2] == 'hematofago':
			animal = 'sanguessuga'
		else:
			animal = 'minhoca'

print(animal)