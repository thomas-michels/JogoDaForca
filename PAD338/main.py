from PAD338.Arquivos.JogoForca import JogoForca


def jogar():
    jf = JogoForca()
    jogada = True
    while jogada:
        jogada = jf.jogar()
        status = jf.get_status_game()
        if status:
            print('Você descobriu a palavra!')
            break

        elif status is False:
            print('Game Over!')


if __name__ == '__main__':
    jogar()
