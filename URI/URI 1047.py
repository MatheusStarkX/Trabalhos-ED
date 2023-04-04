#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

hi, mi, hf, mf = input().split()
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)

if mi > mf: 
	mf = mf + 60
	hf = hf - 1
if hi > hf:
	hf = hf + 24	
if hi == hf and mf-mi == 0:
  hf = hf + 24

horas = hf-hi
minutos = mf - mi

print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')