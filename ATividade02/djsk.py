
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
        self.caminho = {}
        self.peso = self._MAX


    def menor(self):
        pass


    def relaxa(self):
        pass


    def caminho(self, aresta, u):
        if(aresta != self.fim):
            men = self.menor(aresta, u)




    def verifica_caminho(self):
        pass

    



graf = Grafo()
graf.add_node('a', [['b',7], ['c',3]])
graf.add_node('b', [['a',7], ['c',2], ['e',1], ['d', 2]])
graf.add_node('c', [['a',3], ['b',2], ['e', 5]])
graf.add_node('d', [['b',2], ['2',2], ['f', 1]])
graf.add_node('e', [['b',1], ['c',5], ['d', 2], ['f', 9]])
graf.add_node('f', [['d',1], ['e',9]])