from Arquivos.Sorteador import sortear_palavra
from Arquivos.PesquisarLetra import Pesquisar


class JogoForca:

    __palavra = sortear_palavra()
    __pesquisador = Pesquisar(__palavra)
    __vidas = 5
    __status_game = None

    def get_status_game(self) -> bool:
        return self.__status_game

    def __diminuir_vidas(self) -> None:
        self.__vidas -= 1

    def __transformar_list(self, valor) -> list:
        lista = []
        for i in valor:
            lista.append(i)

        return lista

    def __validar_vidas(self) -> bool:

        if self.__vidas < 1:
            self.__status_game = False
            return False

        return True

    def __validar_jogada(self, letras) -> bool:
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

    def jogar(self) -> bool:
        if self.__validar_vidas():
            print(f'Vidas Restantes: {self.__vidas}')
            print(self.__pesquisador.retornar_palavra())
            letras = input('Insira uma letra ou a palavra: ').lower()
            if self.__validar_jogada(letras):
                return True

        return False
