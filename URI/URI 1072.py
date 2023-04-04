#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

n = int(input())
cont1 = 0
cont2 = 0
for num in range(n):
	x = int(input())
	if 10 <= x <= 20:
		cont1 = cont1+1
	else:
		cont2 = cont2+1

print(cont1,'in')
print(cont2,'out')