from grafo import Grafo

class BellmanFord(object):

    def __init__(self, grafo, ini) -> None:
        self._MAX = 1000000
        self.ini = ini
        self.grafo = grafo.nos
        self.camm = []
        self.arestas = {}
        for i in self.grafo:
            self.arestas.update({i:{'u':'', 'peso':self._MAX}})
        self.arestas[self.ini] = {'u':'', 'peso':0}
        

    def _relaxa(self, ciclo=False) -> None:
        for i in self.arestas:
            for j in self.grafo[i]:
                x = j[1] + self.arestas[i]['peso']
                if self.arestas[j[0]]['peso'] > x:
                    self.arestas[j[0]]['peso'] = x
                    self.arestas[j[0]]['u'] = i
                    if ciclo == True:
                        return False
        if ciclo == True:
            return True


    def run(self) -> None:
        for i in range(0, (len(self.grafo) - 1)):
            self._relaxa()


    def ciclo_negativo(self):
        return self._relaxa(True)


    def caminho(self, fim):
        self.camm.append(fim)
        ant = self.arestas[fim]['u']
        while(ant != ''):
            self.camm.insert(0, ant)
            ant = self.arestas[ant]['u']


graf = Grafo()
graf.add_node('s', [['t',6], ['y',7]])
graf.add_node('t', [['x',5], ['z',-4], ['y',8]])
graf.add_node('y', [['z',2], ['x',-3]])
graf.add_node('x', [['t',-2]])
graf.add_node('z', [['s',2], ['x',7]])
# graf.add_node('f', [['d',1], ['e',9]])

bff = BellmanFord(graf, 's')
bff.run()
print(bff.arestas)
print(bff.ciclo_negativo())
bff.caminho('z')
print(bff.camm)