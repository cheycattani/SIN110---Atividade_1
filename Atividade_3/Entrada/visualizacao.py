import igraph
import numpy as np
import matplotlib as plot

'''Cria Grafo: Função para criação de um objeto grafo da biblioteca iGraph a partir de uma matriz de adjacências
Entrada: matriz de adjacências (tipo numpy.ndarray)
Saída: grafo (tipo iGraph)'''


def criaGrafo(matriz):
    qtdVertices = np.shape(matriz)[0]
    grafo = igraph.Graph()  # Cria objeto igraph inicialmente vazio
    grafo.add_vertices(qtdVertices)  # Adiciona vértices ao grafo
    grafo.vs["label"] = range(0, grafo.vcount())  # Define o nome de cada nó como um número inteiro
    for vi in range(0, qtdVertices):  # Para cada vértice vi
        for vj in range(vi + 1, qtdVertices):  # Para cada vértice vj
            controle = matriz[vi][vj]
            while controle > 0:  # Adiciona a quantidade de arestas paralelas ou peso da aresta
                grafo.add_edges([(vi, vj)])
                controle -= 1
    return grafo


'''Visualização do Grafo: Função para obter uma imagem de um grafo da biblioteca iGraph
Entrada: execucao (True/False); grafo (tipo igraph.Graph())
Saída: arquivo .png'''


def visualizarGrafo(execucao, grafo):
    if execucao == True:  # True para visualizar a imagem ou False
        grafo.vs[0]
        layout = grafo.layout("fr")  # Layouts: kk, drl, fr, tree
        visual_style = {}  # Vetor com as características visuais do grafo
        visual_style["vertex_size"] = 40  # Tamanho do vértice
        visual_style["vertex_shape"] = "circle"  # Formatos: triangle, circle, square
        visual_style["vertex_label_size"] = 20  # Tamanho do rótulo do vértice
        visual_style["margin"] = 30  # Margem do grafo em relação a borda da figura.
        grafo.vs["color"] = str(
            '#') + '99CCFF'  # Cores: Az=99CCFF; Cinz=CCCCCC ; Am=FFFF00; Vd=33FF00; Lar=FFCC00; Ros=FF00FF
        visual_style["autocurve"] = True  # Considera arestas curvas. False para arestas retas.
        igraph.plot(grafo, target='grafo.png', layout=layout, **visual_style)
    return
