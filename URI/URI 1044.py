#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

x , y = input().split()
x = int(x)
y = int(y)

#O símbolo % é o resto
if x%y == 0 or y%x == 0:
	print('Sao Multiplos')
else:
	print('Nao sao Multiplos')