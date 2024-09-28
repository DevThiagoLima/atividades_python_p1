ataqueGuerreiro1 = int(input("Ataque do Guerreiro 1: "))
defesaGuerreiro1 = int(input("Defesa do Guerreiro 1: "))

ataqueGuerreiro2 = int(input("Ataque do Guerreiro 2: "))
defesaGuerreiro2 = int(input("Defesa do Guerreiro 2: "))

poderGuerreiro1 = ataqueGuerreiro1 + defesaGuerreiro1
poderGuerreiro2 = ataqueGuerreiro2 + defesaGuerreiro2

if poderGuerreiro1 > poderGuerreiro2:
    print("Guerreiro 1 é o vencedor!")
elif poderGuerreiro2 > poderGuerreiro1:
    print("Guerreiro 2 é o vencedor!")
else:
    if defesaGuerreiro1 > defesaGuerreiro2:
        print("Guerreiro 1 é o vencedor pelo critério de defesa!")
    elif defesaGuerreiro2 > defesaGuerreiro1:
        print("Guerreiro 2 é o vencedor pelo critério de defesa!")
    else:
        print("O duelo terminou em empate!")
