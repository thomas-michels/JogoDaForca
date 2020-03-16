from PAD338.Sorteador import sortear_palavra
from PAD338.PesquisarLetra import Pesquisar


class JogoForca:

    def __init__(self):
        self.__palavra = sortear_palavra()
        self.__pesquisador = Pesquisar(self.__palavra)
        self.__vidas = 5

    def __diminuir_vidas(self):
        self.__vidas -= 1

    def __transformar_list(self, valor):
        lista = []
        for i in valor:
            lista.append(i)

        return lista

    def jogar(self):
        print(f'Vidas Restantes: {self.__vidas}')
        print(self.__pesquisador.retornar_palavra())
        letras = input("Insira uma letra ou a palavra: ")
        jogada = self.__pesquisador.procurar_letra(self.__transformar_list(letras))
        if jogada is False:
            self.__diminuir_vidas()
