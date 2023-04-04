#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

#Questionário 2 ED

#Questão 1

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

frase = input().split()
pilha1 = Stack()
pilha2 = Stack()

for sla in frase:
	if sla.isdigit():
		pilha2.push(sla)
	else:
		pilha1.push(sla)

print('Palavras:')
while not pilha1.isEmpty():
	print(pilha1.pop())

print('Numeros:')
while not pilha2.isEmpty():
	print(pilha2.pop())

#Questão 2

class Stack:
     def __init__(self):
         self.items = []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

sentenca = input()
pilha = Stack()

for ch in sentenca:
	if ch != '*':
		pilha.push(ch)
	else:
		print(pilha.pop(), end = '')

#Questão 3

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

entrada = input().split()
inferno = Queue()

for nome in entrada:
	if nome == entrada[-1]:
		x = int(nome)
	else:
		inferno.enqueue(nome)

if x == 0:
	primeiro = inferno.dequeue()
else:
	for i in range(x):
		inferno.enqueue(inferno.dequeue())

	primeiro = inferno.dequeue()

while not inferno.isEmpty():
  	ultimo = inferno.dequeue()

print('Pessoa da frente:', primeiro)
print('Pessoa do fim:', ultimo)

#Questão 4

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

l1 = input().split()
feito = int(input())

fake1 = []
fake2 = []
fake3 = []
tarefas = Queue()
prioridade = Queue()

for i in range(len(l1)):
    if i%2 == 0:
        fake1.insert(0,l1[i])
    else:
        fake2.insert(0,l1[i])
        fake3.insert(0,l1[i])

fake3.sort()
tamanho = len(fake3)
for k in range(tamanho):
    prioridade.enqueue(fake3[k])
    
for i in range(tamanho):
    j = len(fake2) - 1
    while j >= 0:
        if fake3[i] == fake2[j]:
            tarefas.enqueue(fake1[j])
            del fake1[j]
            del fake2[j]
            break
        j -= 1

while feito != 0:
    tarefas.dequeue()
    prioridade.dequeue()
    feito -= 1

print('Tamanho da fila:', tarefas.size())

while not tarefas.isEmpty():
    print(f'Atividade: {tarefas.dequeue()} Prioridade: #{prioridade.dequeue()}')

#Questão 5

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

pilha = Stack()
cont = 0
soma = 0

while pilha.isEmpty() or pilha.peek() != 0:
	pilha.push(int(input()))

pilha.pop()

desejada = int(input())

while not pilha.isEmpty() and pilha.peek() != desejada:
	soma += pilha.peek()
	cont += 1
	print('Peso retirado:', pilha.pop())

if not pilha.isEmpty():
  soma += pilha.peek()
  cont += 1
  print('Peso retirado:', pilha.pop())

print('Anilhas retiradas:', cont)
print('Peso total movimentado:', soma)

#Questão 6

def exibe_candidatos( deque, pos, ordem ):
    cont1 = 0
    cont2 = deque.size() - 1
    if ordem == 'direta':
        while not deque.is_empty():
            if cont1 == pos:
                print(deque.remove_front())
            else:
                deque.remove_front()
                cont1 += 1
    if ordem == 'inversa':
        while not deque.is_empty():
            if cont2 == pos:
                print(deque.remove_rear())
            else:
                deque.remove_rear()
                cont2 -= 1

#Questão 7

letra = 'A'
listinha = []
bebe = []

while letra != 'X':
	linha = input().split()
	letra = linha[0]
	if len(linha) >= 2:
		v = int(linha[1])
		if len(linha) == 3:
			n = int(linha[2])

	if letra == 'I':
		listinha.insert(0, v)
	if letra == 'F':
		listinha.append(v)
	if letra == 'P':
		bebe.append(listinha.pop())
	if letra == 'D':
		bebe.append(listinha.pop(0))
	if letra == 'E':
		bebe.append(listinha.pop(v-1))
	if letra == 'T':
		listinha[listinha.index(v)] = n
    
for k in range(len(bebe)):
	print(bebe[k])
print()
for i in range(len(listinha)):
	print(listinha[i])

#Questão 8

letra = 'A'
listinha = []
bebe = []
cont = 0

while letra != 'X':
	linha = input().split()
	letra = linha[0]
	if len(linha) >= 2:
		v = int(linha[1])
		if len(linha) == 3:
			n = int(linha[2])

	if letra == 'I':
		listinha.insert(0, v)
	if letra == 'F':
		listinha.append(v)
	if letra == 'P':
		bebe.append(listinha.pop())
	if letra == 'D':
		bebe.append(listinha.pop(0))
	if letra == 'E':
		bebe.append(listinha.pop(v-1))
	if letra == 'T':
		listinha[listinha.index(v)] = n
	if letra == 'V':
		for i in range(listinha.count(v)):
			listinha.remove(v)
			cont += 1
		bebe.append(cont)
	if letra == 'C':
		bebe.append(listinha.count(v))
    
for k in range(len(bebe)):
	print(bebe[k])
print()
for i in range(len(listinha)):
	print(listinha[i])

#Questão 9

letra = 'A'
chave = []
tempo = []
pos = []
cont = 0

while letra != 'f':
	x = 0
	linha = input().split()
	letra = linha[0]
	if len(linha) >= 2:
		c = int(linha[1])
		if len(linha) == 3:
			j = int(linha[2])

	if letra == 'i':
		chave.append(c)
		tempo.append(cont)
		if j == 0 or len(chave)-1-j < 0:
			pos.append(-1)
		else:
			pos.append(len(chave)-1-j)
	if letra == 'r':
		tempo.pop(chave.index(c))
		for k in range(len(chave)):
			if pos[k] == chave.index(c):
				x += 1
				pos[k] = -1
			if x > 0 and pos[k] != -1 and pos[k] != 0:
				pos[k] = pos[k] - 1
		pos.pop(chave.index(c))
		chave.remove(c)
	cont += 1

if not chave:
	print('-1')
else:
	for i in range(len(chave)):
		if pos[i] == -1:
			print(f'[{chave[i]},{tempo[i]}]', end = ' ')
		else:
			print(f'[{chave[i]},{tempo[i]},{pos[i]}]', end = ' ')

#Questão 10 - ERRADO

saida = []
palavras = input().split()

for frescura in palavras:
	pal = []
	letras = []
	for char in frescura:
		letras.append(char)
	tam = 3
	while tam <= len(letras):
		j = tam
		for k in range(len(letras)):
			igual = True
			achado = ''
			i = k+tam
			y = i-1
			x = k
			if i > len(letras):
				break
			while x != i and igual:
				frente = letras[x]
				tras = letras[y]
				if frente != tras:
					igual = False
				else:
					achado += letras[x]
				x += 1
				y -= 1
			if igual:
				pal.append(achado)

			j += 1
		tam += 1

	for boa in pal:
		if pal.count(boa) > 1:
			pal.remove(boa)

	l = 0
	while l != len(pal):
		x = len(pal)
		if l+1 < len(pal):
			for s in range(l+1,len(pal)):
				if pal[s].count(pal[l]) > 0:
					pal.pop(l)
		if len(pal) != x:
			l = 0
		else:
			l += 1

	if len(pal) >= 2:
		saida.append(frescura)

for t in saida:
	print(t)
