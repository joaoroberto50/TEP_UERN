#include <stdio.h>
#include <stdlib.h>
#include "util.h"

// João Roberto

struct no{
	struct item dados;
	struct no *prox;
};

typedef struct no No;


Lista* nova_lista(void){
	Lista* li = (Lista*) malloc(sizeof(Lista));
	if(li != NULL)
		*li = NULL;
	return li;
}


// ADiciona o elemento já ordenado
int add_elem(Lista* li, struct item numm){
	if(li == NULL) return 0;
	No* node = (No*) malloc(sizeof(No));
	if(node == NULL) return 0;
	No *ant, *att = *li;
	node->dados = numm;
	if(*li == NULL){
		// node->dados = numm;
		node->prox = (*li);
		*li = node;
	}
	else{
		while(att != NULL && att->dados.numero < numm.numero){
			ant = att;
			att = att->prox;
		}
		if(att == *li){
			node->prox = (*li);
			*li = node;
		}
		else{
			node->prox = ant->prox;
			ant->prox = node;
		}
	}
	return 1;
}


int encotra_elem(Lista* li, int numm){
	if(li == NULL) return 0;
	No *node = *li;
	int cont = 0;
	while(node != NULL && node->dados.numero != numm){
		node= node->prox;
		cont++;
	}
	if(node == NULL)
		return -1;
	else
		return cont;
}


void imprime_lista(Lista* li){
	if(li == NULL) return;
	No *aux = *li;
	while(aux != NULL){
		printf("-> %d ", aux->dados.numero);
		aux = aux->prox;
	}
}


void dell_ini(Lista* li){
	No *node = *li;
	*li = node->prox;
	free(node);
}


void dell_elem(Lista* li, int numm){
	if(li == NULL) return;
	No *ant, *att = *li;
	int pos = encotra_elem(li, numm);
	if(pos != -1){
		while(att->dados.numero != numm){
			ant = att;
			att = att->prox;
		}
		if(pos == 0)
			dell_ini(li);
		else{
			ant->prox = att->prox;
			free(att);
		}
	}
}


void dell_lista(Lista* li){
	if(li != NULL){
		No* node;
		while((*li) != NULL){
			node = *li;
			*li = (*li)->prox;
			free(node);
		}
		free(li);
	}
}


/* 
    Ordenação & Busca
    OBS.:   l deriva de left(esquerda)
            r deriva de rigth(direita)
*/

void quick_sort(int *vet, int init, int fim){
	int pivo;
	if(fim > init){
		pivo = divide(vet, init, fim);
		quick_sort(vet, init, pivo-1);
		quick_sort(vet, pivo+1, fim);
	}
}


int divide(int *vet, int init, int fim){
	int l, r, pivo, aux;
	l = init;
	r = fim;
	pivo = vet[init];
	while(l<r){
		while(vet[l] <= pivo) l++;
		while(vet[r] > pivo) r--;
		if(l<r){
			aux = vet[l];
			vet[l] = vet[r];
			vet[r] = aux;
		}
	}
	vet[init] = vet[r];
	vet[r] = pivo;
	return r;
}


int busca_iterativa(int *vet, int numm, int tam){
	int l = 0;
	int r = tam - 1;
	int meio;
	while(l <= r){
		meio = (l + r)/2;
		if(numm == vet[meio]) return meio;
		if(numm < vet[meio]) r = meio;
		else l = meio+1;
	}
	return -1;
}


int busca_recursiva(int *vet, int numm, int l, int r){
	int meio = (l + r)/2;
	if(l > r) return -1;
	if(numm == vet[meio]) return meio;
	if(numm > vet[meio]) return busca_recursiva(vet, numm, meio+1, r);
	else return busca_recursiva(vet, numm, l, meio);	
}


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
	printf("\nEncontra um elemento [10] [indice]\n");
	x = encotra_elem(li, 10);
	printf("%d", x);
	dell_elem(li, 1);
	printf("\nLista apos a exclusao de um elemento [1]\n");
	imprime_lista(li);
	dell_lista(li);
	printf("\n");
	printf("\nBusca e Ordenacao\n");
	printf("Vetor Original\n");
	int vet[10] = {9,5,11,0,7,55,2,8,13,3};
	for(int i=0; i<10; i++){
		printf("%d ", vet[i]);
	}
	quick_sort(vet, 0, 9);
	printf("\nVetor ordenado pelo quicksort:\n");
	for(int i=0; i<10; i++){
		printf("%d ", vet[i]);
	}
	printf("\nBusca binaria iterativa [elemento 13]\n");
	x = busca_iterativa(vet, 13,(sizeof(vet)/4));
	printf("%d\n", x);
	printf("Busca binaria recursiva [elemento 9]\n");
	x = busca_recursiva(vet, 9, 0, ((sizeof(vet)/4)-1));
	printf("%d\n", x);
	return 0;
}
