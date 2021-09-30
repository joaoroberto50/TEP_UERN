from util.grafo import Grafo
from util.dijkstra import Dijkstra


graf = Grafo()
graf.add_node('a', [['b',7], ['c',3]])
graf.add_node('b', [['a',7], ['c',2], ['e',1], ['d', 2]])
graf.add_node('c', [['a',3], ['b',2], ['e', 5]])
graf.add_node('d', [['b',2], ['e',2], ['f', 1]])
graf.add_node('e', [['b',1], ['c',5], ['d', 2], ['f', 9]])
graf.add_node('f', [['d',1], ['e',9]])

graf.print_grafo()


djs = Dijkstra(graf, 'a', 'f')
djs.caminho()
print(djs.ares)
custo = djs.ares['f']['peso']
print(f'CAMINHO: {djs.camm} com CUSTO: {custo}')