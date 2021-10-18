from util.grafo import Grafo
from util.dijkstra import Dijkstra
from random import choice
import threading


'''
    Hospital 1 (vértice 40) V39
    Hospital 2 (vértice 19) V18
    Hospital 3 (vértice 82) V81

    Central do SAMU: (vértice 83) V82
'''

HOSPITAIS = ['V39', 'V18', 'V81']
SAMU = 'V82'


def sorteia_acidente(vertices):
    print(vertices)
    while True:
        x = choice(vertices)
        if x not in HOSPITAIS and x != SAMU:
            return x





graf = Grafo('./Dist110_clean.dat')
djsk = Dijkstra(graf)
local = sorteia_acidente([*graf.nos])
print(local)
djsk.caminho(SAMU, local)
custo = djsk.ares[local]['peso']
print(f'CAMINHO do SAMU ate o local {local}: {djsk.camm} com CUSTO: {custo}')
