distanciadragA = float(input('Digite a distancia percorrida do primeiro dragão: '))
tempodragA = float(input('Digite o tempo do primeiro dragão: '))

distanciadragB = float(input('Digite a distancia percorrida do segundo dragão: '))
tempodragB = float(input('Digite o tempo do segundo dragão: '))

velocidadeA = distanciadragA / tempodragA
velocidadeB = distanciadragB / tempodragB

if velocidadeA > velocidadeB:
    print(f'O Primeiro Dragão É Mais Rápido!')

elif velocidadeB > velocidadeA:
    print('O Segundo Dragão é Mais Rápido!')

else:
    print('O Dois Dragões Tem A Mesma Velocidade!')
