'''
Nome: Cheyenne Cattani Pereira
Matrícula: 2021001943
Disciplina: SIN110
'''

import numpy
import numpy as np

'''Tipo Grafo: Retorna o tipo do grafo representado por uma dada matriz de adjacências
Entrada: matriz de adjacências
Saida: Integer (0 - simples, 1 - digrafo, 2 - multigrafo, 3 - pseudografo) '''


def tipoGrafo(matriz):
    direcionado = not simetrica(matriz)
    tem_laco = laco(matriz)
    paralela = arestas_paralelas(matriz)

    # Condicional para identificar o grafo
    if not direcionado and not tem_laco and not paralela:  # simples
        return 0
    elif direcionado and not tem_laco and paralela:  # diagrafo
        return 1
    elif not direcionado and not tem_laco and paralela:  # multigrafo
        return 2
    else:
        return 3  # pseudografo


# verificar se a matriz é simétrica

def simetrica(matriz):
    ehsimples = True
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            if matriz[i][j] != matriz[j][i]:
                ehsimples = False
                break
    return ehsimples


# verifica se a matriz tem laços

def laco(matriz):
    tem_laco = False
    for i in range(matriz.shape[0]):
        tem_laco = matriz[i][i] != 0
        if tem_laco:
            break
    return tem_laco


# verifica se a matriz tem arestas paralelas

def arestas_paralelas(matriz):
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            if matriz[i][j] > 1:
                return True
    return False


'''Verifica Adjacência: Função que verifica se os vértices vi e vj são adjacentes.
Entrada: matriz de adjacências (numpy.ndarray), vi (Integer), vj (Integer)
Saída: 0 (Integer) se vi e vj NÃO são adjacentes; 1 se vi e vj são adjacentes'''


def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] > 0:  # Se célula M[vi][vj] for maior que 0 existe uma ou mais arestas
        verticesAdjacentes = True
    else:
        verticesAdjacentes = False
    print('Vertices', vi, 'e', vj, 'são adjacentes?', verticesAdjacentes, '\n')
    return verticesAdjacentes


'''Calcula Densidade: Retorna o valor da densidade do grafo
Entrada: matriz de adjacências
Saida: Float (valor da densidade com precisão de três casas decimais)'''


def calcDensidade(matriz):
    # Verifica qual é o tipo do grafo
    tipo = tipoGrafo(matriz)

    # Contador
    cont = 0

    # Contando as arestas
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            if matriz[i][j] != 0:
                cont += 1
    # Simples
    if tipo == 0:
        cont /= 2
        return round((2 * cont) / (matriz.shape[0] * (matriz.shape[0] - 1)), 3)

    # Dígrafo
    elif tipo == 1:
        return round(cont / (matriz.shape[0] * (matriz.shape[0] - 1)), 3)
    else:
        return - 1


'''Insere Aresta: Insere uma aresta no grafo considerando o par de vértices vi e vj
Entrada: Matriz de adjacêcnias, vi e vj (ambos são números inteiros que indicamo id do vértice
Saída: void'''


def insereAresta(matriz, vi, vj):
    matriz[vi][vj] += 1


''' Remove Aresta: Remove uma aresta no grafo considerando o par de vértices vi e vj
Entrada: Matriz de adjacêcnias, vi e vj (ambos são números inteiros que indicamo id do vértice
Saída: boolean (True se remoção Ok, False se a aresta não existe)'''


def removeAresta(matriz, vi, vj):
    matriz[vi][vj] = 0


'''Insere Vertice: Insere um vértice no grafo
Entrada: matriz de adjacências, vi(número inteiro que indica o id do vértice)
Saída: Boolean (True se remoção OK, False se a aresta não existe)'''


def insereVertice(matriz, vi):
    shape = matriz.shape

    # Será criada uma nova matriz de zeros
    nMatriz = np.zeros((shape[0] + 1, shape[1] + 1))

    # Esse for irá transferir os valores da matriz antiga para a nova.
    for i in range(0, matriz.shape[0]):
        for vj in range(0, matriz.shape[0]):
            nMatriz[vi][vj] = matriz[vi][vj]

    return nMatriz  # retorna a nova matriz


'''Remove Vertice: Remove um vértice do grafo
Entrada: matriz de adjacências, vi (número inteiro que indica o id do vértice
Saída: Boolean (True se remoção OK, False caso o vértice vi, não exista)'''


def removeVertice(matriz, vi):
    pass
