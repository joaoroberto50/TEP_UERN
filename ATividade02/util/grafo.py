
class Grafo:
    def __init__(self, file_name=None):
        self.nos = {}
        if file_name:
            self.file = file_name
            self._open_file()
    

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


    def _file_grafo(self, h, m):
        for i in range(0, len(m)):
            pesos = []
            for j in range(0, len(m[i])):
                if((m[i][j] != '-' and m[i][j] != '0') and j != 0):
                    pesos.append([h[j], int(m[i][j])])
            self.add_node(m[i][0], pesos)


    def _organiza(self, linhas):
        header = linhas[0][:-1].split('\t')
        matrix = []
        for i in range(1, len(linhas)):
            matrix.append(linhas[i][:-1].split('\t'))
        self._file_grafo(header, matrix)


    def _open_file(self):
        linhas = []
        with open(self.file) as fp:
            for item in fp:
                linhas.append(item)
        self._organiza(linhas)
