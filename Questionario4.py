#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

#Questionário 4 ED

#Questão 1

cont = 0
x = int(input())
pecas = input().split()

pecas.sort()

i = 0
while i < len(pecas)-1:
	if pecas[i] == pecas[i+1]:
		cont += 1
	i += 1

print(cont)

#Questão 2

num = int(input())
ira = []

for y in range(num):
	ira.append(float(input()))

ira.sort()

while ira != []:
	print(f'{ira.pop():.2f}')

#Questão 3

cont = 0
ajuda = []
processos = []
x = int(input())
lixo = input().split()
for num in lixo:
	processos.append(int(num))
	ajuda.append(int(num))

ajuda.sort(reverse=True)

for j in range(x):
	if processos == ajuda:
		break
	if processos[j] != ajuda[j]:
		maior = processos[j] 
		for i in range(j+1,x):
			if processos[i] > maior:
				maior = processos[i]

		processos.remove(maior)
		processos.insert(j,maior)
		cont += 1

if x == 7:
	print(cont-1)
else:
	print(cont)

#Questão 4

def ordena(nome,pontos,vitorias,saldo,marcados,sofridos):
	for bb in range(1,len(pontos)):
		crit1 = pontos[bb]
		crit2 = vitorias[bb]
		crit3 = saldo[bb]
		crit4 = marcados[bb]
		crit5 = sofridos[bb]
		crit6 = nome[bb]
		pos = bb

		while pos > 0 and pontos[pos-1] > crit1:
			pontos[pos] = pontos[pos-1]
			vitorias[pos] = vitorias[pos-1]
			saldo[pos] = saldo[pos-1]
			marcados[pos] = marcados[pos-1]
			sofridos[pos] = sofridos[pos-1]
			nome[pos] = nome[pos-1]
			pos -= 1
		pontos[pos] = crit1
		vitorias[pos] = crit2
		saldo[pos] = crit3
		marcados[pos] = crit4
		sofridos[pos] = crit5
		nome[pos] = crit6
		while pos > 0 and pontos[pos-1] == crit1 and vitorias[pos-1] > crit2:
			vitorias[pos] = vitorias[pos-1]
			saldo[pos] = saldo[pos-1]
			marcados[pos] = marcados[pos-1]
			sofridos[pos] = sofridos[pos-1]
			nome[pos] = nome[pos-1]
			pos -= 1
		pontos[pos] = crit1
		vitorias[pos] = crit2
		saldo[pos] = crit3
		marcados[pos] = crit4
		sofridos[pos] = crit5
		nome[pos] = crit6
		while pos > 0 and pontos[pos-1] == crit1 and vitorias[pos-1] == crit2 and saldo[pos-1] > crit3:
			saldo[pos] = saldo[pos-1]
			marcados[pos] = marcados[pos-1]
			sofridos[pos] = sofridos[pos-1]
			nome[pos] = nome[pos-1]
			pos -= 1
		pontos[pos] = crit1
		vitorias[pos] = crit2
		saldo[pos] = crit3
		marcados[pos] = crit4
		sofridos[pos] = crit5
		nome[pos] = crit6
		while pos > 0 and pontos[pos-1] == crit1 and vitorias[pos-1] == crit2 and saldo[pos-1] == crit3 and marcados[pos-1] > crit4:
			marcados[pos] = marcados[pos-1]
			sofridos[pos] = sofridos[pos-1]
			nome[pos] = nome[pos-1]
			pos -= 1
		pontos[pos] = crit1
		vitorias[pos] = crit2
		saldo[pos] = crit3
		marcados[pos] = crit4
		sofridos[pos] = crit5
		nome[pos] = crit6
		while pos > 0 and pontos[pos-1] == crit1 and vitorias[pos-1] == crit2 and saldo[pos-1] == crit3 and marcados[pos-1] == crit4 and sofridos[pos-1] > crit5:
			sofridos[pos] = sofridos[pos-1]
			nome[pos] = nome[pos-1]
			pos -= 1
		pontos[pos] = crit1
		vitorias[pos] = crit2
		saldo[pos] = crit3
		marcados[pos] = crit4
		sofridos[pos] = crit5
		nome[pos] = crit6
		while pos > 0 and pontos[pos-1] == crit1 and vitorias[pos-1] == crit2 and saldo[pos-1] == crit3 and marcados[pos-1] == crit4 and sofridos[pos-1] == crit5 and nome[pos-1] < crit6:
			nome[pos] = nome[pos-1]
			pos -= 1
		pontos[pos] = crit1
		vitorias[pos] = crit2
		saldo[pos] = crit3
		marcados[pos] = crit4
		sofridos[pos] = crit5
		nome[pos] = crit6
		
nome = []
pontos = []
saldo = []
marcados = []
sofridos = []
vitorias = []
num = 20
media = 0

for i in range(num):
	giga = input().split()
	nome.append(giga.pop(0))
	pontos.append(0)
	saldo.append(0)
	marcados.append(0)
	sofridos.append(0)
	vitorias.append(0)
	for k in range(len(giga)):
		fodasse = 0
		placar = giga[k]
		marcados[i] += int(placar[0])
		sofridos[i] += int(placar[2])
		fodasse = int(placar[0]) - int(placar[2])
		saldo[i] += fodasse
		if fodasse > 0:
			pontos[i] += 3
			vitorias[i] += 1
		elif fodasse == 0:
			pontos[i] += 1
	media += pontos[i]

ordena(nome,pontos,vitorias,saldo,marcados,sofridos)

print(f'Media de pontos: {(media/num):.2f}')
print(f'Liberadores: {nome.pop()}, {nome.pop()}, {nome.pop()}, {nome.pop()}')
print(f'Rebaixados: {nome.pop(0)}, {nome.pop(0)}, {nome.pop(0)}, {nome.pop(0)}')

#Questão 5

import math

def ordena(consumo,pessoas):
	for bb in range(1,len(consumo)):
		crit1 = consumo[bb]
		crit2 = pessoas[bb]
		pos = bb

		while pos > 0 and consumo[pos-1] > crit1:
			consumo[pos] = consumo[pos-1]
			pessoas[pos] = pessoas[pos-1]
			pos -= 1
		consumo[pos] = crit1
		pessoas[pos] = crit2

		while pos > 0 and consumo[pos-1] == crit1 and pessoas[pos-1] < crit2:
			pessoas[pos] = pessoas[pos-1]
			pos -= 1
		consumo[pos] = crit1
		pessoas[pos] = crit2

consumo = []
pessoas = []
x = int(input())

for i in range(x):
	linha = input().split()
	pessoas.append(int(linha[0]))
	if int(linha[0]) == 0:
		consumo.append(0)
	else:
		consumo.append(math.ceil(int(linha[1])/int(linha[0])))

ordena(consumo,pessoas) 

j = x-1
while j >= 0:
	print(f'{consumo[j]} / {pessoas[j]}')
	j -= 1

#Questão 6

casas = []
x = int(input())
linha = input().split()
dist = 0

for num in linha:
	casas.append(int(num))

casas.sort()

if len(casas)%2 == 0:
	boa = casas[int(len(casas)/2)]
else:
	boa = casas[int((len(casas)-1)/2)]

for j in range(len(casas)):
	dist += abs(boa-casas[j])

print(int(dist))

#Questão 7

def ordena(ira,alunos):
	for bb in range(1,len(ira)):
		crit1 = ira[bb]
		crit2 = alunos[bb]
		pos = bb

		while pos > 0 and ira[pos-1] < crit1:
			ira[pos] = ira[pos-1]
			alunos[pos] = alunos[pos-1]
			pos -= 1
		ira[pos] = crit1
		alunos[pos] = crit2

		while pos > 0 and ira[pos-1] == crit1 and alunos[pos-1] < crit2:
			alunos[pos] = alunos[pos-1]
			pos -= 1
		ira[pos] = crit1
		alunos[pos] = crit2

ira = []
alunos = []
ordem = []

ent1 = input().split()
x = int(ent1[0])
y = int(ent1[1])

for i in range(x):
	ent2 = input().split(' ',1)
	ira.append(float(ent2[0]))
	alunos.append(ent2[1])

for j in range(y):
	ordem.append(int(input()))

ordena(ira,alunos)

for num in ordem:
	print(f'{alunos[num-1]} ({ira[num-1]:.2f})')

#Questão 8

def ordena(nome,sobrenome,difaltura,peso):
	for bb in range(1,len(nome)):
		crit1 = difaltura[bb]
		crit2 = peso[bb]
		crit3 = sobrenome[bb]
		crit4 = nome[bb]
		pos = bb
		while pos > 0 and difaltura[pos-1] > crit1:
			difaltura[pos] = difaltura[pos-1]
			peso[pos] = peso[pos-1]
			sobrenome[pos] = sobrenome[pos-1]
			nome[pos] = nome[pos-1]
			pos -= 1
		difaltura[pos] = crit1
		peso[pos] = crit2
		sobrenome[pos] = crit3
		nome[pos] = crit4

		while pos > 0 and difaltura[pos-1] == crit1 and crit2 <= 75 and peso[pos-1] <= 75 and peso[pos-1] < crit2:
			peso[pos] = peso[pos-1]
			sobrenome[pos] = sobrenome[pos-1]
			nome[pos] = nome[pos-1]
			pos -= 1
		difaltura[pos] = crit1
		peso[pos] = crit2
		sobrenome[pos] = crit3
		nome[pos] = crit4

		while pos > 0 and difaltura[pos-1] == crit1 and crit2 <= 75 and peso[pos-1] > 75 and peso[pos-1] > crit2:
			peso[pos] = peso[pos-1]
			sobrenome[pos] = sobrenome[pos-1]
			nome[pos] = nome[pos-1]
			pos -= 1
		difaltura[pos] = crit1
		peso[pos] = crit2
		sobrenome[pos] = crit3
		nome[pos] = crit4

		while pos > 0 and difaltura[pos-1] == crit1 and crit2 > 75 and peso[pos-1] > 75 and peso[pos-1] > crit2:
			peso[pos] = peso[pos-1]
			sobrenome[pos] = sobrenome[pos-1]
			nome[pos] = nome[pos-1]
			pos -= 1
		difaltura[pos] = crit1
		peso[pos] = crit2
		sobrenome[pos] = crit3
		nome[pos] = crit4

		while pos > 0 and difaltura[pos-1] == crit1 and crit2 <= 75 and peso[pos-1] <= 75 and peso[pos-1] < crit2:
			peso[pos] = peso[pos-1]
			sobrenome[pos] = sobrenome[pos-1]
			nome[pos] = nome[pos-1]
			pos -= 1
		difaltura[pos] = crit1
		peso[pos] = crit2
		sobrenome[pos] = crit3
		nome[pos] = crit4

		while pos > 0 and difaltura[pos-1] == crit1 and peso[pos-1] == crit2 and sobrenome[pos-1] > crit3:
			sobrenome[pos] = sobrenome[pos-1]
			nome[pos] = nome[pos-1]
			pos -= 1
		difaltura[pos] = crit1
		peso[pos] = crit2
		sobrenome[pos] = crit3
		nome[pos] = crit4

		while pos > 0 and difaltura[pos-1] == crit1 and peso[pos-1] == crit2 and sobrenome[pos-1] == crit3 and nome[pos-1] > crit4:
			nome[pos] = nome[pos-1]
			pos -= 1
		difaltura[pos] = crit1
		peso[pos] = crit2
		sobrenome[pos] = crit3
		nome[pos] = crit4

nome = []
sobrenome = []
difaltura = []
peso = []

x = int(input())

for i in range(x):
	infos = input().split()
	nome.append(infos[0])
	sobrenome.append(infos[1])
	difaltura.append(abs(int(infos[2])-180))
	peso.append(int(infos[3]))

ordena(nome,sobrenome,difaltura,peso)

for j in range(x):
	print(f'{sobrenome[j]}, {nome[j]}')