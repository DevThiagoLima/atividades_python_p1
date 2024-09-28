def selecaoMagia(magia):

    match magia:
        case 1:
            print('Você usou a magia de fogo!')
        case 2:
            print('Você usou a magia de água!')
        case 3:
            print('Você usou a magia de terra!')

if __name__ == '__main__':

    magia = int(input('Qual Magia Você Deseja Usar? [1] Fogo, [2] Água, [3] Terra : '))

    selecaoMagia(magia)
