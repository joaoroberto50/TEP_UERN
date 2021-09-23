#include <stdio.h>
#include <stdlib.h>
#include "util.h"

// João Roberto


int main(int argc, char const *argv[])
{
	int x;
	Lista *li;
	li = nova_lista();
	struct item a;
	a.numero = 10;
	x = add_elem(li, a);
	a.numero = 11;
	x = add_elem(li, a);
	a.numero = 19;
	x = add_elem(li, a);
	a.numero = 15;
	x = add_elem(li, a);
	a.numero = 1;
	x = add_elem(li, a);
	a.numero = 5;
	x = add_elem(li, a);
	printf("Lista Original\n");
	imprime_lista(li);
	printf("Encontra um elemento\n");
	x = encotra_elem(li, 1);
	printf("%d", x);
	dell_elem(li, 1);
	printf("\nLista apos a exclusao de um elemento\n");
	imprime_lista(li);
	dell_lista(li);
	printf("\n");
	printf("Busca e Ordenacao\n");
	int vet[10] = {9,5,11,0,7,55,2,8,13,3};
	for(int i=0; i<10; i++){
		printf("%d ", vet[i]);
	}
	quick_sort(vet, 0, 9);
	printf("\nOrdenado pelo quicksort:\n");
	for(int i=0; i<10; i++){
		printf("%d ", vet[i]);
	}
	printf("\nBusca binaria iterativa\n");
	x = busca_iterativa(vet, 13,(sizeof(vet)/4));
	printf("%d\n", x);
	printf("Busca binaria recursiva\n")
	x = busca_recursiva(vet, 0, 0, ((sizeof(vet)/4)-1));
	printf("%d\n", x);
	return 0;
}