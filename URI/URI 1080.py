#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

#Código que não sei por que não funcionou
numeros = []
i = 0

for valor in range(100):
	numeros.append(int(input()))
	i = i+1
  	if i == 1:
    	numeros[i-1] = numeros[i]
	elif numeros[i] > numeros[i-1]:
		posmaior = i 

print(numeros[posmaior])
print(posmaior)

#Código funcional
x = 0

for i in range(100):
	numero = int(input())
	if numero > x:
		maior = numero
		posicao = i+1
		x = numero

print(maior)
print(posicao)