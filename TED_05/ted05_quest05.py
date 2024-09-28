quantAgua = float(input('Informe a Quantidade de Água Disponível em Litros: '))
distOasis = float(input('Informe a Distancia Que Falta Para Chegar No Oasis: '))

aviso = quantAgua / distOasis

if aviso < 2:
    print('Você não terá água suficiente para chegar no oasis!')
else:
    print('Você terá água suficiente para chegar no oasis!')
