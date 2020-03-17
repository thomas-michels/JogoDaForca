
class Pesquisar:
    def __init__(self, palavra: str):
        self.__palavra = palavra
        self.__criar_lista_letras_disponiveis()

    def get_letras_disponiveis(self):
        return self.__letras_disponiveis

    def __criar_lista_letras_disponiveis(self):
        self.__letras_disponiveis = []
        for i in self.__palavra:
            self.__letras_disponiveis.append(False)

    def procurar_letra(self, letras_escolhidas: list):
        indice = 0
        letras_encontras = []

        for letra in self.__palavra:
            if letra in letras_escolhidas:
                self.__letras_disponiveis[indice] = True
                if letra not in letras_encontras:
                    letras_encontras.append(letra)

            indice += 1

        if letras_encontras != letras_escolhidas:
            return False

        return True

    def retornar_palavra(self):
        indice = 0
        string_retorno = ''
        for letra in self.__palavra:
            if self.__letras_disponiveis[indice] is False:
                string_retorno += '_ '

            else:
                string_retorno += letra + ' '

            indice += 1

        return string_retorno
