#include <stdlib.h>

// João Roberto

struct item{
	int numero;
};

typedef struct no* Lista;

Lista* nova_lista(void);

int add_elem(Lista* li, struct item numm);

int encotra_elem(Lista* li, int numm);

void imprime_lista(Lista* li);

void dell_ini(Lista* li);

void dell_elem(Lista* li, int numm);

void dell_lista(Lista* li);

void dell_lista(Lista* li);

void quick_sort(int *vet, int init, int fim);

int divide(int *vet, int init, int dim);

int busca_iterativa(int *vet, int numm, int tam);

int busca_recursiva(int *vet, int numm, int l, int r);