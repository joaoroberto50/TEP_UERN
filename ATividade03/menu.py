from grafo import Grafo
from heuristicas import *

grafo = Grafo('./Gr17_clean.dat')

heu_gulosa = Gulosa(grafo)
print('Busca Gulosa\n\n')
print('-----------------------')
x = input()
heu_gulosa.verifica_rotas()
x = input
print(heu_gulosa.camm)
print(heu_gulosa.custo)
x = input()

heu_local = BuscaLocal(grafo)
print('\n\n\n\nBusca local\n\n')
print('-----------------------')
x = input()


for i in range(0, 153):
    heu_local.troca_vertices()

print(heu_local.camm)
print(heu_local.custo)
x = input()
print('\n\n\n\n\n')
heu_aleatoria = GulosaAleatoria(grafo)
print('Busca Gulosa Aleatoria\n\n')
print('-----------------------')
heu_aleatoria.constroi_rota('V0', 0.5)
x = input()
print('Coeficiente = 0.5')
print(heu_aleatoria.camm)
print(heu_aleatoria.custo)
x = input()
heu_aleatoria.constroi_rota('V0', 0.2)
print('Coeficiente = 0.2')
x = input()
print(heu_aleatoria.camm)
print(heu_aleatoria.custo)