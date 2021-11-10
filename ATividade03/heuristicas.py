

_MAX = 999999


class Gulosa(object):
    
    def __init__(self, grafo) -> None:
        self.camm = []
        self.camm_tmp = []
        self.n_visitado = []
        self.n_visitado_tmp = []
        self.origins = []
        self.grafo = grafo.nos
        self.custo = _MAX
        self.custo_tmp = 0
        for i in self.grafo:
            self.n_visitado.append(i)
            self.origins.append(i)
        self.origem = 'V0'
        self.att = self.origem

    
    def _menor_aresta(self, aresta) -> str:
        menor = _MAX
        m_ares = ''
        for i in self.grafo[aresta]:
            if i[1] < menor and i[0] in self.n_visitado_tmp:
                menor = i[1]
                m_ares = i[0]
        self.camm_tmp.append(m_ares)
        self.custo_tmp += menor
        print(menor)
        return m_ares


    def encontra_rota(self, origem=''):
        self.camm_tmp = []
        if origem:
            self.origem = origem
            self.att = self.origem
        # print(self.n_visitado_tmp)
        self.n_visitado_tmp.remove(self.origem)
        while(self.n_visitado_tmp):
            x = self._menor_aresta(self.att)
            self.n_visitado_tmp.remove(x)
            self.att = x
            # print('.')
        self.n_visitado_tmp.append(self.origem)
        self._menor_aresta(self.att)

    
    def verifica_rotas(self):
        # self.origins.pop(0)
        for i in self.origins:
            self.n_visitado_tmp = self.n_visitado.copy()
            self.custo_tmp = 0
            self.encontra_rota(i)
            print(self.camm_tmp)
            print(self.custo_tmp)
            if self.custo_tmp < self.custo:
                self.camm = self.camm_tmp.copy()
                self.custo = self.custo_tmp



    def teste(self):
        for i in self.grafo:
            print(i)