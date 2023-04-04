#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

#Questionário 3 ED

#Questão 1

def mdc(num1,num2):
	div = num2%num1
	if div == 0:
		return num1
	else:
		return mdc(div,num2)

quant = input().split()
if int(quant[0]) <= int(quant[1]):
	num1 = int(quant[0])
	num2 = int(quant[1])
else:
	num1 = int(quant[1])
	num2 = int(quant[0])

print(mdc(num1,num2))

#Questão 2

def jogo(premios, num):
	i = len(premios) - 1
	while i >= 0:
		if num >= premios[i]:
			num -= premios[i]
		i -= 1
		if num == 0:
			return True
	return False

premios = []
l1 = input().split()
for k in l1:
	premios.append(int(k))
premios.sort()
num = int(input())

while len(premios) >= 1:
	if jogo(premios, num):
		print('E possivel ganhar.')
		break
	premios.pop()

if not premios:
	print('Impossivel ganhar.')

#Questão 3 - FALHOU EM 1 TESTE

soma = 0

def Fib(n):
	global soma
	soma += 1
	if n <= 1:
		return n
	else:
		return Fib(n-1) + Fib(n-2)

n = int(input())
res = Fib(n)

print(f'Fib({n}) = {res} ({soma} chamadas)')

#Questão 4 

def fibonacci(n):
	def fib(n):
		if n <= 1:
			return n
		else:
			return fib(n-1) + fib(n-2)
	num = []
	x = []
	while n > 0:
		num.insert(0, fib(n-1))
		n -= 1
		x += fibonacci(n-1)
	return num

#Questão 5

def soma(somatorio,lele):
	if not lele:
		return somatorio
	else:
		somatorio += lele[0]
		if len(lele) > 1:
			print(f'{lele.pop(0)} + soma({lele})')
		else:
			print(lele.pop(0))
	return soma(somatorio,lele)

n = int(input())
lele = []
i = 1
somatorio = 0
while i <= n:
	lele.append(2*i - 1)
	i += 1
resul = soma(somatorio,lele)
print('---------------')
print(n, '** 2 ==', resul)

#Questão 6

n = int(input())
numeros = []
certo = []
fats = [1,1]

for k in range(n):
	x = int(input())
	numeros.append(x)
	certo.append(x)
certo.sort()

i = 2
valor = 1
while i <= certo[len(certo)-1]:
	valor = valor*i
	if valor <= 2357:
		fats.append(valor)
	else:
		fats.append(valor%2357)
	i += 1

for num in numeros:
	for k in range(num+1):
		print(fats[k], end=' ')
	print(' ')

#Questão 7

n = int(input())
fib = []
total = []

for i in range(5*n):
	total.append(i)

ult = 1
penul = 1

for j in range(5*n):
	if j <= 1:
		fib.append(j)
	else:
		valor = ult+penul
		if valor > 5*n - 1:
			break
		fib.append(valor)
		penul = ult
		ult = valor

m = 0
while m < len(fib):
	if fib[m] in total:
		total.remove(fib[m])
	m += 1

for k in range(n):
	if k == n-1:
		print(total[k])
	else:
		print(total[k], end = ', ')

#Questão 8 - FALHOU EM 2 TESTES

def decompress(n):
	letras = 'ABCDEFGHIJKLMNOPKRSTUVXWYZ'
	if n//32 == 0:
		if n < 26:
			return letras[n-1]
		else:
			return letras[n-27] 
	else:
		return letras[(n%32)-1] + decompress(n//32)