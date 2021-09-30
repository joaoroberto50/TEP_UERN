
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
