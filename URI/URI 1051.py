#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

x = float(input())

if x > 4500:
	imposto = (1000*0.08) + (1500*0.18) + ((x-4500)*0.28)
if 3000 < x <= 4500:
	imposto = (1000*0.08) + ((x-3000)*0.18)
if 2000 < x <= 3000:
	imposto = (x-2000)*0.08 
if x <= 2000:
	print('Isento')
else:
	print(f'R$ {imposto:.2f}')