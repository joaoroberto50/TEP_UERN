from util.grafo import Grafo
from util.bellman_ford import BellmanFord


graf = Grafo()
graf.add_node('s', [['t',6], ['y',7]])
graf.add_node('t', [['x',5], ['z',-4], ['y',8]])
graf.add_node('y', [['z',2], ['x',-3]])
graf.add_node('x', [['t',-2]])
graf.add_node('z', [['s',2], ['x',7]])


bff = BellmanFord(graf, 's')
bff.run()
print(bff.arestas)
print(bff.ciclo_negativo())
bff.caminho('z')
print(bff.camm)