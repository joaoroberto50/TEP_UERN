from util.grafo import Grafo
from util.bellman_ford import BellmanFord


graf = Grafo('./testes/teste03.txt')
# graf.add_node('s', [['t',6], ['y',7]])
# graf.add_node('t', [['x',5], ['z',-4], ['y',8]])
# graf.add_node('y', [['z',2], ['x',-3]])
# graf.add_node('x', [['t',-2]])
# graf.add_node('z', [['s',2], ['x',7]])


bff = BellmanFord(graf, 'A')
print(bff.arestas)
bff.run()
print(bff.arestas)
print(bff.ciclo_negativo())
bff.caminho('E')
print(bff.camm)