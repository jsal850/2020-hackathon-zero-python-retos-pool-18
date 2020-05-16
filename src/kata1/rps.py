from random import randint

options = ["Piedra", "Papel", "Tijeras"]
# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    if (player == 0 and ai == 2) or (player == 1 and ai == 0) or (player == 2 and ai == 0):
        return "Ganaste!"
    elif player == ai:
        return "Empate!"
    else: 
        return "Perdiste"
    
    

# Entry Point
def Game():
    #
    #
    player = 0
    #Bucle Para Asegurar que la seleccion es correcta
    while True:
        player = input("Introducir 1 para Piedra, 2 Para Papel, 3 Para tijeras:")
        player = int(player)
        if player > 0 and player < 4:
            break
    
    player = player - 1
    ai = randint(0, 2)
    print("Has Seleccionado: " + options[player] + " AI ha Seleccionado: " + options[ai])
    
    winner = quienGana(player, ai)

    print(winner)

Game()