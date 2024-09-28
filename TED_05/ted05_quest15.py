energia = int(input("Energia do portal (%): "))
coordenadasPrecisas = input("Coordenadas de destino estão precisas? (sim/não): ").lower()
tempoAjustado = input("O tempo está ajustado corretamente? (sim/não): ").lower()

if energia > 80 and coordenadasPrecisas == "sim" and tempoAjustado == "sim":
    print("O portal pode ser ativado!")
else:
    if energia <= 80:
        print("Energia insuficiente para ativar o portal.")
    if coordenadasPrecisas != "sim":
        print("Coordenadas imprecisas.")
    if tempoAjustado != "sim":
        print("Tempo não ajustado corretamente.")
