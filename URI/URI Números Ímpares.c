/*Nome: Matheus Felipe Magalhães de Assis
 *Matrícula: 19/0035242
 *Disciplina: Algoritmos e Programação de Computadores
 *E-mail: matheusfelipemdeassis@gmail.com*/

#include<stdio.h>

int main(){
	int i,n;
	scanf("%d", &n);
	for(i = 1; i <= n; i++){
		if (i%2 != 0)
			printf("%d\n", i);
	}

	return 0;
}