from PAD338.JogoForca import JogoForca
from PAD338.Sorteador import sortear_palavra
from PAD338.PesquisarLetra import Pesquisar

def jogar():
    palavra = sortear_palavra()
    print(palavra)
    pesquisar = Pesquisar(palavra)
    print(pesquisar.retornar_palavra())
    letra = input('Letra: ')
    pesquisar.procurar_letra(letra)
    print(pesquisar.retornar_palavra())
    letra = input('Letra: ')
    pesquisar.procurar_letra(letra)
    print(pesquisar.retornar_palavra())




if __name__ == '__main__':
    #jogar()
    jf = JogoForca()
    while True:
        jf.jogar()