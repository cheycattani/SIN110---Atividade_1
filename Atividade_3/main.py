'''
Nome: Cheyenne Cattani Pereira
Matrícula: 2021001943
Disciplina: SIN110
'''

from Entrada import (entra_dados, visualizacao)
from Saida import resultado
from Metodos import caracteristicas as car

if __name__ == '__main__':
    argumento = input('Digite qual arquivo deseja verificar: ')
    resultado_ = entra_dados.dados(argumento)

    func = car.verificaAdjacencia(resultado_, 0, 1)
    res = [argumento, resultado_, car.tipoGrafo(resultado_), car.calcDensidade(resultado_)]
    resultado.saida(res)

    print('Nome da instância:', res[0], '\n')
    print('Matriz: \n', res[1], '\n')

    # Mostra as caracteristicas do grafo
    G = visualizacao.criaGrafo(resultado_)
    print(G, '\n')

    print('Tipo do grafo:', res[2])
    print('Densidade:', res[3], '\n')

    # Insere as coordenadas para inserir e remover arestas e vértices
    vi = int(input('Digite a coordenada x: '))
    vj = int(input('Digite a coordenada y: '))
    print('\n')

    car.insereAresta(resultado_, vi, vj)
    print('Inserindo arestas...\n', res[1], '\n')
    # Visualiza o grafo depois que inseriu uma aresta
    visualizacao.visualizarGrafo(True, visualizacao.criaGrafo(resultado_))

    input('Aperte enter!\n')
    car.removeAresta(resultado_, vi, vj)
    print('Removendo arestas...\n', res[1], '\n')
    # Visualiza o grafo depois que remove uma aresta
    visualizacao.visualizarGrafo(True, visualizacao.criaGrafo(resultado_))

    input('Aperte enter!\n')
    car.insereVertice(resultado_, vi)
    print('Inserindo vértices...\n', res[1], '\n')
    # Visualiza o grafo depois que inseriu um vértice
    visualizacao.visualizarGrafo(True, visualizacao.criaGrafo(resultado_))

    input('Aperte enter!\n')
    car.removeVertice(resultado_, vi)
    print('Removendo vértices...\n', res[1])
    # Visualiza o grafo depois que removeu um vértice
    visualizacao.visualizarGrafo(True, visualizacao.criaGrafo(resultado_))
