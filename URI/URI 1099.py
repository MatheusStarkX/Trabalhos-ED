#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

n = int(input())
saida = []
soma = 0
i = 0
for k in range(n):
	num = input().split()
	num.sort()
	x = int(num[0])
	y = int(num[1])
	for valor in range(x+1,y):
		if valor%2 != 0:
			soma += valor
	saida.append(soma)
	soma = 0
while i<len(saida):
  print(saida[i])
  i += 1