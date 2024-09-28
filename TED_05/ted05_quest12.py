ataqueEspada = int(input("Poder de ataque da Espada: "))
durabilidadeEspada = int(input("Durabilidade da Espada: "))

ataqueArco = int(input("Poder de ataque do Arco: "))
durabilidadeArco = int(input("Durabilidade do Arco: "))

ataqueLanca = int(input("Poder de ataque da Lança: "))
durabilidadeLanca = int(input("Durabilidade da Lança: "))

if ataqueEspada > 50 and durabilidadeEspada > 70:
    print("A Espada é a melhor escolha.")

elif ataqueArco > 50 and durabilidadeArco > 70:
    print("O Arco é a melhor escolha.")

elif ataqueLanca > 50 and durabilidadeLanca > 70:
    print("A Lança é a melhor escolha.")

else:
    print("Nenhuma das armas é adequada, busque uma nova arma.")
