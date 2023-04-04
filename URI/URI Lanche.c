/*Nome: Matheus Felipe Magalhães de Assis
 *Matrícula: 19/0035242
 *Disciplina: Algoritmos e Programação de Computadores
 *E-mail: matheusfelipemdeassis@gmail.com*/

#include<stdio.h>

int main(){
	int q,c;
	float p;
	scanf("%d", &c);
	scanf("%d", &q);
	if(c == 1)
		p = 4;
	if(c == 2)
		p = 4.5;
	if(c == 3)
		p = 5;
	if(c == 4)
		p = 2;
	if(c == 5)
		p = 1.5;
	printf("Total: R$ %.2f\n", p*q);




	return 0;
}