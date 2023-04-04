#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com


n1,n2,n3,n4 = input().split()

media = (2*float(n1) + 3*float(n2) + 4*float(n3) + 1*float(n4))/10
print(f"Media: {media:.1f}")

if media >= 7.0:
	print("Aluno aprovado.")
if media < 5.0:
	print("Aluno reprovado.")
if 5.0 <= media <= 6.9:
	print("Aluno em exame.")
	notaexame = float(input())
	print(f"Nota do exame: {notaexame:.1f}")
	novamedia = (media + notaexame)/2
	if novamedia >= 5.0:
		print("Aluno aprovado.")
	else:
		print("Aluno reprovado.")
	print(f"Media final: {novamedia:.1f}")