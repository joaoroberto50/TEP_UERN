from util.grafo import Grafo
from util.dijkstra import Dijkstra

graf = Grafo('./testes/teste02.txt')
graf.print_grafo()

djs = Dijkstra(graf, 'A', 'G')

djs.caminho()
print(djs.ares)
custo = djs.ares['G']['peso']
print(f'CAMINHO: {djs.camm} com CUSTO: {custo}')