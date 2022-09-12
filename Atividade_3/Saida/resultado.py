from Entrada import entra_dados

'''Salva Resultado: Função para salvar em arquivo .txt o resultado da execução do programa.
Entrada: resultado (tipo lista)
Saída: arquivo .txt no diretório especificado'''


def saida(resultado):
    stringRes = resultado[0] + ' - '
    for res in resultado[1]:
        stringRes += str(res) + ' '
    file = open(r"C:/Atividade_3/Resultado/resultado.txt", "a+") # open irá abrir o arquivo
    file.writelines(stringRes + '\n') # escreve no arquivo as informações

    file.write(resultado[0] + ' - tipo: ' + str(resultado[2]) + '\n')
    file.close() # .close irá fechar o arquivo
