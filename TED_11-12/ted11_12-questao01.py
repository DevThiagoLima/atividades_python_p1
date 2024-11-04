listaNum = []


for i in range(10):
    num = int(input('Digite um valor: '))
    listaNum.append(num)

repetido = False

for i in range(9):
    for j in range(i + 10):
        if listaNum[i] == listaNum[j]:
            print(f'Número {listaNum[i]} repetido nas posições {i} e {j}')
            repetido = True

if not repetido:
    print('Não há números repetidos!')
