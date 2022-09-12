import numpy as np
import os
import sys

if __name__ == '__main__':
    argumento = sys.argv[1]  # lista de argumentos.
    caminho = os.path.join(os.getcwd(), argumento + ".txt")  # caminho que vai fazer para ler o arquivo.
    instancia = np.loadtxt(caminho)  # vai ler o arquivo e armazenar no numpy array.
    dimensoes = np.shape(instancia)
    print(argumento + " " + str(dimensoes))
    resultado = os.path.join(os.getcwd(), "resultado" + ".txt")

    with open(resultado, 'a+') as file:  # open vai abrir o caminho novamente, o a serve para colocar no final do arquivo
        armazenatxt = argumento + " " + str(dimensoes) + "\n"  # texto que vou escrevo no arquivo
        file.write(armazenatxt)