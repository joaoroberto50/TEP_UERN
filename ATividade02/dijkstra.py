
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
    def __init__(self, grafo, ini, fim):
        self._MAX = 1000000
        self.grafo = grafo.nos
        self.ini = ini
        self.fim = fim
        self.open = self.grafo
        self.v = {'u':'', 'v':'', 'c':0}
        self.cam = []
        self.c = {self.ini:{self.ini: 0, 'att':self.ini, 'ant':''}}
        for i in grafo.nos:
            if i != ini:
                self.c.update({i: {i: self._MAX, 'att':i, 'ant':''}})


    def _menor(self, vert, ares, v):
        min = self._MAX
        print(vert)
        for i in vert:
            if (i[1] < min and i[0] != ares):
                min = i[1]
                aux = i
        self.open[v].remove(aux)
        return aux


    def run(self, aresta='a', val=0, u=''):
        print(aresta)
        if(aresta != self.fim):
            men = self._menor(self.grafo[aresta], u, aresta)
            men[1] += val
            if (self.c[men[0]][men[0]] > men[1]):
                self.c[men[0]]['ant'] = aresta
                self.c[men[0]][men[0]] = men[1]
                self.cam.append(aresta)
                self.run(self.c[men[0]]['att'], self.c[men[0]][men[0]], aresta)
        if(aresta == self.fim):
            self.cam.append(aresta)
        self.run([*self.open][0], )
        







graf = Grafo()
graf.add_node('a', [['b',7], ['c',3]])
graf.add_node('b', [['a',7], ['c',2], ['e',1], ['d', 2]])
graf.add_node('c', [['a',3], ['b',2], ['e', 5]])
graf.add_node('d', [['b',2], ['2',2], ['f', 1]])
graf.add_node('e', [['b',1], ['c',5], ['d', 2], ['f', 9]])
graf.add_node('f', [['d',1], ['e',9]])

graf.print_grafo()

dsj = Dijkstra(graf, 'a', 'f')
dsj.run()
print(dsj.cam)
print(dsj.open)