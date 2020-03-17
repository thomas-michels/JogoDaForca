from Arquivos.Palavras import Palavras
from random import randint


def sortear_palavra():
    palavras = Palavras()
    lista_palavras = palavras.get_lista_frutas()
    indice = randint(0, (len(lista_palavras) - 1))
    return lista_palavras[indice]
