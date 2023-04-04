#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

#Questionário 1 ED

#Questão 2

def divisores(n):
	div = []
	for num in range(1,n+1):
		if n%num == 0:
			div.append(num)
	
	return div

#Questão 3

def primo(n):
	cont = 0
	for num in range(1,n+1):
		if n%num == 0:
			cont += 1
	
	if cont == 2:
		return 'Primo.'
	else:
		return 'Não primo.'

#Questão 4

nome = input('Qual o seu nome? ')
print(f'Bem vindo ao Aprender3, {nome}.')
print('May the force be with you.')

#Questão 5

def analisa(x, y):
	if x > y:
		palavra = str(x)+'\n'+str(y)+'\n'+'diferentes'
	if x < y:
		palavra = str(y)+'\n'+str(x)+'\n'+'diferentes'
	if x == y:
		palavra = str(x)+'\n'+str(y)+'\n'+'iguais'
	
	return print(palavra)

#Questão 6

def max3(x, y, z):
	lista = [x,y,z]
	lista.sort()
	return lista[2]

#Questão 7

linha1 = input().split()
d1 = int(linha1[0])
horario1 = linha1[1].split(':')
h1 = int(horario1[0])
m1 = int(horario1[1])
s1 = int(horario1[2])

linha2 = input().split()
d2 = int(linha2[0])
horario2 = linha2[1].split(':')
h2 = int(horario2[0])
m2 = int(horario2[1])
s2 = int(horario2[2])

seg = s2-s1
mnt = m2-m1
hora = h2-h1
dia = d2-d1 

if seg < 0:
	seg = seg+60
	mnt = mnt-1
if mnt < 0:
	mnt = mnt+60
	hora = hora-1
if hora < 0:
	hora = hora+24
	dia = dia-1  
if (dia < 0) or (dia==0 and hora==0 and mnt==0 and seg==0):
	print('Data inválida!')
else:
	print(f'{dia} dia(s)')
	print(f'{hora} hora(s)')
	print(f'{mnt} minuto(s)')
	print(f'{seg} segundo(s)')

#Questão 8

num = int(input())

cordcoelho = input().split()
coelhox = float(cordcoelho[0])
coelhoy = float(cordcoelho[1])

cordraposa = input().split()
raposax = float(cordraposa[0])
raposay = float(cordraposa[1])

cont = 0
for k in range(num):
	cordburaco = input().split()
	buracox = float(cordburaco[0])
	buracoy = float(cordburaco[1])	
	predador = (((buracox - raposax)**2) + ((buracoy - raposay)**2))**0.5
	presa = (((buracox - coelhox)**2) + ((buracoy - coelhoy)**2))**0.5
	if predador/2 < presa:
		cont += 1
	else:
		print(f'O coelho pode escapar pelo buraco ({cordburaco[0]}, {cordburaco[1]}).')
		break
if cont == num:
	print('O coelho nao pode escapar.')
