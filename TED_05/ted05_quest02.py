ferro = int(input('Digite a Quantidade de Ferro em KG: '))
ouro = int(input('Digite a Quantidade de Ouro em KG: '))

liga = ferro + ouro
porcentagem = (ferro / liga) * 100

if porcentagem >= 70:
    print(f'Você precisa de pelo menos 70% de ferro na liga dos metais!')

else:
    print(f'Sua armadura será forjada!')
