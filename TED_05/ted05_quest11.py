nota1Candidato1 = float(input('Informe a Primeira Nota do Candidato 1: '))
nota2Candidato1 = float(input('Informe a Segunda Nota do Candidato 1: '))
nota3Candidato1 = float(input('Informe a Terceira Nota do Candidato 1: '))

nota1Candidato2 = float(input('Informe a Primeira Nota do Candidato 2: '))
nota2Candidato2 = float(input('Informe a Segunda Nota do Candidato 2: '))
nota3Candidato2 = float(input('Informe a Terceira Nota do Candidato 2: '))

nota1Candidato3 = float(input('Informe a Primeira Nota do Candidato 3: '))
nota2Candidato3 = float(input('Informe a Segunda Nota do Candidato 3: '))
nota3Candidato3 = float(input('Informe a Terceira Nota do Candidato 3: '))

mediaCandidato1 = (nota1Candidato1 + nota2Candidato1 + nota3Candidato1) / 3
mediaCandidato2 = (nota1Candidato2 + nota2Candidato2 + nota3Candidato2) / 3
mediaCandidato3 = (nota1Candidato3 + nota2Candidato3 + nota3Candidato3) / 3

if mediaCandidato1 > mediaCandidato2 and mediaCandidato1 > mediaCandidato3:
    print(f'O Candidato 1 teve a maior média, logo vendeu a disputa!')

elif mediaCandidato2 > mediaCandidato1 and mediaCandidato2 > mediaCandidato3:
    print(f'O Candidato 2 teve a maior média, logo vendeu a disputa!')

elif mediaCandidato3 > mediaCandidato1 and mediaCandidato3 > mediaCandidato2:
    print(f'O Candidato 3 teve a maior média, logo vendeu a disputa!')

else:
    print(f'Ouve um empate!')
