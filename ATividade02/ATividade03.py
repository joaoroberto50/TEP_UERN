from util.grafo import Grafo
from util.dijkstra import Dijkstra
from util.bellman_ford import BellmanFord
from random import choice
import threading
import copy


'''
    Hospital 1 (vértice 40) V39
    Hospital 2 (vértice 19) V18
    Hospital 3 (vértice 82) V81

    Central do SAMU: (vértice 83) V82
'''

HOSPITAIS = ['V39', 'V18', 'V81']
SAMU = 'V82'
graf = Grafo('./Dist110_clean.dat')
djsk = Dijkstra(graf)
blm = BellmanFord(graf)


def sorteia_acidente(vertices):
    while True:
        x = choice(vertices)
        if x not in HOSPITAIS:
            return x


def executa(local):
    caminhos = []
    pesos = []
    djsk.caminho(SAMU, local)
    custo = djsk.ares[local]['peso']
    print(f'CAMINHO do SAMU ate o local {local}: {djsk.camm} com CUSTO: {custo}')
    blm.run(local)
    for i in HOSPITAIS:
        camm, peso = blm.caminho(i)
        caminhos.append(camm), pesos.append(peso)
    print(pesos)
    print(min(pesos))
    print(caminhos[pesos.index(min(pesos))])


def menu():
    print(f'Hosptais: {HOSPITAIS}\nSAMU: {SAMU}')
    while True:
        x = input(""" 1 - Soertear um local aleatorio\n
         2 - Digitar um local
         0 - Sair\n>>>""")
        if x == '0':
            break
        elif x == '1':
            local = sorteia_acidente([*graf.nos])
            print(local)
            executa(local)
        elif x == '2':
            local = input("Digite um valor entre V0 e V109, com exceção dos hospitais\n>>>")
            executa(local)
        else:
            print('Digite um valor valido')


menu()
'''
graf = Grafo('./Dist110_clean.dat')
djsk = Dijkstra(graf)
local = sorteia_acidente([*graf.nos])
print(local)
djsk.caminho(SAMU, local)
print(djsk.caminho(SAMU, local))
custo = djsk.ares[local]['peso']
print(f'CAMINHO do SAMU ate o local {local}: {djsk.camm} com CUSTO: {custo}')
blm = BellmanFord(graf)
caminhos = []
pesos = []
# print(graf.nos)
blm.run(local)
for i in HOSPITAIS:
    camm, peso = blm.caminho(i)
    caminhos.append(camm), pesos.append(peso)

print(pesos)
print(min(pesos))
print(caminhos[pesos.index(min(pesos))])

'''
