def bonusCavaleiro(missoesCompletas):

    if missoesCompletas > 10:
        print('Você recebeu um bônus de 100 moedas!')

    elif missoesCompletas >= 5 and missoesCompletas <= 10:
        print('Você recebeu um bônus de 50 moedas!')

    elif missoesCompletas < 5 and missoesCompletas > 0:
        print('Você recebeu um bônus de 10 moedas!')

    else:
        print('Você não completou missões!')


if __name__ == '__main__':

    missoesCompletas = int(input('Informe a Quantidade de Missões Completas: '))

    bonusCavaleiro(missoesCompletas)
