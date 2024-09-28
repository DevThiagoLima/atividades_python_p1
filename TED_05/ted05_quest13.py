posicaoExercito = input("O exército está dentro ou fora do castelo? ").lower()

match posicaoExercito:
    case "dentro":
        print("Sistema de defesa desativado.")
    case "fora":
        print("Sistema de defesa ativado.")
    case _:
        print("Posição inválida.")
