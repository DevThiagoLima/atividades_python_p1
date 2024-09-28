def selecaoPorta(porta):

    match porta:
        case 1:
            print('Você Terá Que Enfrentar o Rei Goblin!')
        case 2:
            print('Atravesse o Pantano Venenoso e Traga a Lôtus Branca!')
        case 3:
            print('Fuja Da Grande Pedra Rolante!')
        case 4:
            print('Derrote 8 Inimigos Sem Ser Visto!')
        case 5:
            print('VOCÊ VAI TRABALHAR DE CARTEIRA ASSINADA NUM SUPERMERCADO COM ESCALA 6X1!!!!! (UM DESTINO PIOR QUE A MORTE)')


if __name__ == '__main__':

    porta = int(input('Qual Porta Você Escolhe? [1], [2], [3], [4] ou [5]'))
    selecaoPorta(porta)
