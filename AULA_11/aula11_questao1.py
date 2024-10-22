clubes = []

for i in range(5):
    time = input('Digite o nome do time: ')
    clubes.append(time)

consulta = input('Digite o nome do clube que quer consultar: ')

controle = False

for clube in clubes:
    if clube == consulta:
        controle = True

if controle:
    print('Achei')
else:
    print('Não Achei')
