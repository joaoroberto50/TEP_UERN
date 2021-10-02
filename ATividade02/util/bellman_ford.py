from grafo import Grafo

class BellmanFord(object):

    def __init__(self, grafo, ini, fim) -> None:
        self._MAX = 1000000
        self.ini = ini
        self.fim = fim
        self.grafo = grafo.nos
        self.arestas = {}
        for i in self.grafo:
            self.arestas.update({i:{'u':'', 'peso':self._MAX}})
        self.arestas[self.ini] = {'u':'', 'peso':0}
        

    def relaxa(self, ciclo=False) -> None:
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
            self.relaxa()


    def ciclo_negativo(self):
        return self.relaxa(True)


    def caminho(self):
        pass



graf = Grafo()
graf.add_node('s', [['t',6], ['y',7]])
graf.add_node('t', [['x',5], ['z',-4], ['y',8]])
graf.add_node('y', [['z',2], ['x',-3]])
graf.add_node('x', [['t',-2]])
graf.add_node('z', [['s',2], ['x',7]])
# graf.add_node('f', [['d',1], ['e',9]])

bff = BellmanFord(graf, 's', 'f')
bff.run()
print(bff.arestas)
print(bff.ciclo_negativo())