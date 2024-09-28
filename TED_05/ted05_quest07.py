def classPlantas(alturaPlanta):

    if alturaPlanta < 1:
        print('A Planta é Pequena!')

    elif alturaPlanta >=1 and alturaPlanta <=3:
        print('A Planta é Média!')

    elif alturaPlanta > 3:
        print('A Planta é Grande!')


if __name__ == '__main__':

    alturaPlanta = float(input('Digite a altura da planta: '))
    classPlantas(alturaPlanta)
