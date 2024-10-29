lista_compras = []
r = "Sim"

while r in ["S", "s", "Sim", "sim"]:
    item = input('Digite o item que deseja adicionar a lista: ')
    lista_compras.append(item)
    r = input('Deseja Continuar? (S / N): ')

r = "Sim"
controle = "Continuar"
while controle in ["Continuar", "continuar", "C", "c"]:
    print('\n-=-=-=-=-=-=-=-=-=-=- \n 1. Adicionar Item \n 2. Remover Item \n 3. Exibir Lista \n 4. Sair')
    select = int(input('Digite o que você Deseja Fazer: '))
    match select:
            case 1:
                while r in ["S", "s", "Sim", "sim"]:
                    novo_item = input('Digite o item que deseja adicionar a lista: ')
                    lista_compras.append(novo_item)
                    r = input('Deseja Continuar? (S / N): ')

            case 2:
                while r in ["S", "s", "Sim", "sim"]:
                    print(f'A Lista Atual é: {i + 1}')
                    for i in range(len(lista_compras)):
                        print(i)
                    remover_item = input('Digite qual item deseja tirar: ')
                    lista_compras.remove(remover_item)

            case 3:
                print('A Lista Atualmente é:')
                for i in range(len(lista_compras)):
                    print(lista_compras[i])

            case 4:
                print('Saindo ...')
                controle = "Saindo"

            case _:
                print('Valor Inválido!')
