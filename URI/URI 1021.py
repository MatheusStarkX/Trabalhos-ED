#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

valor = float(input())
valor = int(valor*100)
#cálculo das cédulas
nota1 = valor//10000 
resto1 = valor%10000
nota2 = resto1//5000 
resto2 = resto1%5000
nota3 = resto2//2000 
resto3 = resto2%2000
nota4 = resto3//1000 
resto4 = resto3%1000
nota5 = resto4//500  
resto5 = resto4%500
nota6 = resto5//200  
resto6 = resto5%200
#cálculo das moedas
moeda1 = resto6//100 
troco1 = resto6%100
moeda2 = troco1//50 
troco2 = troco1%50
moeda3 = troco2//25 
troco3 = troco2%25
moeda4 = troco3//10 
troco4 = troco3%10
moeda5 = troco4//5 
troco5 = troco4%5
moeda6 = troco5

print('NOTAS:')
print(f'{nota1} nota(s) de R$ 100.00')
print(f'{nota2} nota(s) de R$ 50.00')
print(f'{nota3} nota(s) de R$ 20.00')
print(f'{nota4} nota(s) de R$ 10.00')
print(f'{nota5} nota(s) de R$ 5.00')
print(f'{nota6} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{moeda1} moeda(s) de R$ 1.00')
print(f'{moeda2} moeda(s) de R$ 0.50')
print(f'{moeda3} moeda(s) de R$ 0.25')
print(f'{moeda4} moeda(s) de R$ 0.10')
print(f'{moeda5} moeda(s) de R$ 0.05')
print(f'{moeda6} moeda(s) de R$ 0.01')