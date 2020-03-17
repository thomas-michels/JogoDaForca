from PAD338.Arquivos.Sorteador import sortear_palavra
from PAD338.Arquivos.PesquisarLetra import Pesquisar


class JogoForca:

    def __init__(self):
        self.__palavra = sortear_palavra()
        self.__pesquisador = Pesquisar(self.__palavra)
        self.__vidas = 5
        self.__status_game = None

    def get_status_game(self):
        return self.__status_game

    def __diminuir_vidas(self):
        self.__vidas -= 1

    def __transformar_list(self, valor):
        lista = []
        for i in valor:
            lista.append(i)

        return lista

    def __validar_vidas(self) -> bool:

        if self.__vidas < 1:
            self.__status_game = False
            return False

        return True

    def __validar_jogada(self, letras):
        novas_letras = self.__transformar_list(letras)
        jogada = self.__pesquisador.procurar_letra(novas_letras)

        if len(novas_letras) > 1 and len(novas_letras) != len(self.__palavra):
            self.__status_game = False
            return False

        if jogada is False:
            self.__diminuir_vidas()

        cont_true = 0
        for letter in self.__pesquisador.get_letras_disponiveis():
            if letter:
                cont_true += 1

        if cont_true == len(self.__palavra):
            self.__status_game = True

        return True

    def jogar(self):
        if self.__validar_vidas():
            print(f'Vidas Restantes: {self.__vidas}')
            print(self.__pesquisador.retornar_palavra())
            letras = input("Insira uma letra ou a palavra: ").lower()
            if self.__validar_jogada(letras):
                return True

        return False
