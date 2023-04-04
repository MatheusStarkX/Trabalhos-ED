#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

#Trabalho Prático ED - A Fuga!

def ordenanahumilde(pesototal,wook):
	for bb in range(1,len(pesototal)):
		crit = pesototal[bb] 
		pric = wook[bb]
		pos = bb

		while pos > 0 and pesototal[pos-1] < crit:
			pesototal[pos] = pesototal[pos-1]
			wook[pos] = wook[pos-1]
			pos -= 1
			
		pesototal[pos] = crit
		wook[pos] = pric

num = int(input())
trabalho = input().split()

sobras = []
wook = []
pesototal = []

if num == 0:
	print('Os Wookies foram para o lado sombrio da força!')
	for peso in trabalho:
		print(int(peso), end=' ')
else:		
	for carga in range(num):
		carga = []
		wook.append(carga)

	j = num-1
	for peso in trabalho:
		if j >= 0:
			wook[j].append(int(peso))
			j -= 1
		else:
			k = num-1
			while k >= 0:
				if int(peso) <= wook[k][len(wook[k])-1]:
					wook[k].append(int(peso))
					break
				else:
					k -= 1
			if k < 0:
				sobras.append(int(peso))

	for anilha in wook:
		soma = 0
		for j in range(len(anilha)):
			soma += anilha[j]
		pesototal.append(soma)

	ordenanahumilde(pesototal,wook)

	for pilha in wook:
		print(pilha, end=' ')

	print()
	if sobras == []:
		print('A força está com os Wookies!')
	else:
		for peso in sobras:
			print(peso, end=' ')
