#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

#Ler a linha 1 e pegar só o número
linha1 = input().split()
d1 = int(linha1[1])
#Ler a linha 2, pegar só os números e transformá-los em inteiros
linha2 = input().split(':')
h1 = int(linha2[0])
m1 = int(linha2[1])
s1 = int(linha2[2])
#Mesma coisa que na linha 1
linha3 = input().split()
d2 = int(linha3[1])
#Mesma coisa que na linha 2
linha4 = input().split(':')
h2 = int(linha4[0])
m2 = int(linha4[1])
s2 = int(linha4[2])

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

print(f'{dia} dia(s)')
print(f'{hora} hora(s)')
print(f'{mnt} minuto(s)')
print(f'{seg} segundo(s)')
