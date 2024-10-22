notas = [5, 10, 8, 7.5, 9]

media = 0
soma = 0

for i in range(len(notas)):
    soma += notas[i]

media = soma / len(notas)

print(f'A Media da Turma Foi de {media}!')
