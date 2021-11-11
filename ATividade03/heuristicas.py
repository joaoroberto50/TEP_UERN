from random import sample, choice




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
        print(f'{menor} - {m_ares}')
        return m_ares


    def encontra_rota(self, origem='') -> None:
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

    
    def verifica_rotas(self) -> None:
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




class BuscaLocal(object):

    def __init__(self, grafo) -> None:
        self.grafo = grafo.nos
        self.mat = []
        inte_i = 0
        self.camm = []
        self.camm_tmp = []
        self.arestas = []
        for i in self.grafo:
            self.mat.append([])
            self.camm.append(i)
            inte_j = 0
            for j in self.grafo[i]:
                if inte_i == inte_j:
                    self.mat[inte_i].append(0)
                self.mat[inte_i].append(j[1])
                inte_j += 1
            inte_i += 1
        self.mat[(inte_i - 1)].append(0)
        self.custo = _MAX
        self._calcula_lista()


    def _calcula_lista(self, cmm=[]) -> list:
        ctl = len(self.camm) - 1
        if not cmm:
            for i in range(0, len(self.camm)):
                if i != ctl:
                    self.arestas.append(self._encontra_valor(self.camm[i], \
                        self.camm[i+1]))
                else:
                    self.arestas.append(self._encontra_valor(self.camm[i], \
                        self.camm[0]))
            self.custo = sum(self.arestas)
        else:
            ares = []
            for i in range(0, len(self.camm)):
                if i != ctl:
                    ares.append(self._encontra_valor(cmm[i], cmm[i+1]))
                else:
                    ares.append(self._encontra_valor(cmm[i], cmm[0]))
            return ares

    
    def _encontra_valor(self, a, b) -> int:
        return self.mat[int(a[1:])][int(b[1:])]


    def _sort_arestas(self) -> list:
        return (sample(range(0, len(self.camm)), 2))

    
    def troca_vertices(self) -> None:
        x, y = self._sort_arestas()
        camm_tmp = self.camm.copy()
        tmp = self.camm[x]
        camm_tmp[x] = self.camm[y]
        camm_tmp[y] = tmp
        val = self._calcula_lista(camm_tmp)
        if sum(val) < self.custo:
            self.arestas = val
            self.camm = camm_tmp
            self.custo = sum(val)
        # print('.')




class GulosaAleatoria(object):

    def __init__(self, grafo) -> None:
        self.grafo = grafo.nos
        self.grafo_tmp = {}
        self.camm = []
        self.custo = _MAX
        self.n_visitado = []
        self.l_pop = []
        for i in self.grafo:
            self.n_visitado.append(i)
        self.rand_coef = 0.5
        self.origem = ''
        self.att = ''
        self._ordena()


    def _ordena(self) -> None:
        for i in self.n_visitado:
            self.grafo[i] = sorted(self.grafo[i], \
                key=lambda l:l[1], reverse=False)


    def _calc_coef(self) -> int:
        if self.coef == 0:
            return 1
        return int(len(len(self.n_visitado))*self.coef)


    def _sorteia_index(self, x):
        while True:
            si = (sample(range(0, x), 1))[0]
            si = self.grafo[self.att][si]
            if si[0] in self.n_visitado:
                return si

    
    def _limpa_colunas(self, z):
        for i in z:
            if i[0] not in self.n_visitado:
                z.remove(i)


    def _escolhe_aresta(self, x) -> None:
        x = self._calc_coef()
        z = self.grafo[self.att].copy()
        self._limpa_colunas(z)
        a = self._sorteia_index(x)
        # a = self.grafo[self.att][a]
        self.camm.append(a[0])
        self.custo += a[1]
        self.att = a[0]
        print(a[0])
        self.n_visitado.remove(a[0])
        self.l_pop.append(int(self.att[1:]))



    def constroi_rota(self, origem='V0', coef=0.5) -> None:
        self.origem = origem
        self.coef = coef
        self.att = self.origem
        self.n_visitado.remove(self.att)
        self.grafo_tmp = self.grafo.copy()
        x = self._calc_coef()
        while(self.n_visitado):
            self._escolhe_aresta(x)
        self.n_visitado.append(self.origem)
        self._escolhe_aresta(x)