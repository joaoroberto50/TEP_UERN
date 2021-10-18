
class Dijkstra:
    def __init__(self, grafo) -> None:
        self._MAX = 1000000
        self.peso = self._MAX
        self.grafo = grafo.nos
        self.ares = {}
        for i in self.grafo:
            self.ares.update({i:{'u':'', 'peso':self._MAX}})


    def _executa(self, ares, v):
        for i in ares:
            val = i[1] + self.ares[v]['peso']
            if self.ares[i[0]]['peso'] > val:
                self.ares[i[0]]['peso'] = val
                self.ares[i[0]]['u'] = v
                # if i[0] != self.fim:
                self.open.append(i[0])
        

    def _relaxa(self):
        aux = self.open.copy()
        while(aux):
            self._executa(self.grafo[aux[0]], aux[0])
            self.open.remove(aux[0])
            aux.pop(0)


    def _ajusta(self, ini, fim):
        self.ini = ini
        self.fim = fim
        self.camm = [self.fim]
        self.open = [self.ini]
        self.ares[self.ini]['peso'] = 0


    def caminho(self, ini, fim):
        self._ajusta(ini, fim)
        while(self.open):
            self._relaxa()
        self._verifica_caminho()


    def _verifica_caminho(self):
        ant = self.ares[self.fim]['u']
        while(ant != ''):
            self.camm.insert(0, ant)
            ant = self.ares[ant]['u']
