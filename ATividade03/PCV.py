from grafo import Grafo

graf = Grafo('./Gr17_clean.dat')
# print(graf.nos)

class Gulosa(object):
    def __init__(self) -> None:
        self.pesos = {}
        self.n_visit = []
        self.camm = []

        for i in graf.nos:
            self.pesos.update({i:0})
            self.n_visit.append(i)
        for i in graf.nos:
            peso = 0
            for j in graf.nos[i]:
                peso += j[1]
            self.pesos[i] = peso
        self.deposito = 'V0'
        self.att = self.deposito
        

    def pega_menor(self) -> str:
        min = 10000
        v = ''
        for i in self.pesos:
            if self.pesos[i] < min and i in self.n_visit:
                min = self.pesos[i]
                v = i
        return v


    def encontra_caminho(self) -> None:
        self.n_visit.remove(self.att)
        self.camm.append(self.att)
        x = self.att
        while(self.n_visit):
            print(x)
            x = self.pega_menor()
            self.n_visit.remove(x)
            self.camm.append(x)
        print(self.camm)


gul = Gulosa()
gul.encontra_caminho()