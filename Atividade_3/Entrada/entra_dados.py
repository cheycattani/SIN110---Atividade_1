import os
import numpy as np

'''Cria Matriz de Adjacência: Função para leitura de um dataset em forma de matriz de adjacências.
Entrada: instancia (nome do arquivo .txt do dataset em forma de matriz de adjacência
Saída: matriz de adjacência (tipo NumPy.ndarray)'''


def dados(argumento):
    caminho = (r"C:/Atividade_3/Instancias/" + argumento + '.txt')  # caminho do arquivo .txt
    with open(caminho, 'rb') as f:
        dado = np.genfromtxt(f, dtype='int64')  # OBS. Lê arquivo .txt de uma Instancia no formato Matriz de Adjacência
    return dado
