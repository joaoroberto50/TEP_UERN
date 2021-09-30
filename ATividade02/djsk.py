
class Grafo:
    def __init__(self):
        self.nos = {}
    
    def add_node(self, att, no):
        self.nos.update({att:no})
    
    def get_grafo(self):
        return self.nos

    def print_grafo(self):
        for i in self.nos:
            print(f'{i}', end=(' '))
            for j in self.nos[i]:
                print(f' {j}', end=(' '))
            print('')


class Dijkstra:
    def __init__(self, grafo, ini, fim) -> None:
        self._MAX = 1000000
        self.peso = self._MAX
        self.ini = ini
        self.fim = fim
        self.camm = [self.fim]
        self.open = [self.ini]
        self.grafo = grafo.nos
        self.ares = {}
        for i in self.grafo:
            self.ares.update({i:{'u':'', 'peso':self._MAX}})
        self.ares[self.ini]['peso'] = 0


    def executa(self, ares, v):
        for i in ares:
            val = i[1] + self.ares[v]['peso']
            if self.ares[i[0]]['peso'] > val:
                self.ares[i[0]]['peso'] = val
                self.ares[i[0]]['u'] = v
                # if i[0] != self.fim:
                self.open.append(i[0])
        

    def relaxa(self):
        aux = self.open.copy()
        while(aux):
            self.executa(self.grafo[aux[0]], aux[0])
            self.open.remove(aux[0])
            aux.pop(0)


    def caminho(self):
        while(self.open):
            self.relaxa()
        self._verifica_caminho()


    def _verifica_caminho(self):
        ant = self.ares[self.fim]['u']
        while(ant != ''):
            self.camm.insert(0, ant)
            ant = self.ares[ant]['u']

    



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