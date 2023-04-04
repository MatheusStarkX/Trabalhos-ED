#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

sal = float(input())

if 0 < sal <= 400:
	percentual = 15
if 400 < sal <= 800:
	percentual = 12
if 800 < sal <= 1200:
	percentual = 10
if 1200 < sal <= 2000:
	percentual = 7
if 2000 < sal:
	percentual = 4	


reajuste = sal*percentual/100
novosal = sal+reajuste
print(f'Novo salario: {novosal:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual} %')