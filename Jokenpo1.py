print("*************************************")
print("Bem vindo ao jokenpô!")
print("*************************************")
print("Sim (1)    Nao (2)")
pergunta = int(input("Você esta pronto para comecar?: "))


while pergunta == 1:

    print(" 1: humano vs computador")
    print(" 2: humano vs humano")
    print(" 3: computador vs computador")
    numero_partidas = 0
    numero_empates = 0
    vitoria_jogador1 = 0
    vitoria_jogador2 = 0
    Modo_jogo = int(input("Digite aqui o modo que você quer jogar: "))
    print("")

    if Modo_jogo == 1:
        print("Voce escolheu o modo humano vs computador!")
        while Modo_jogo == 1:
            print("Pedra = 1")
            print("Tesoura = 2")
            print("Papel = 3")
            numero_jogado = int(input("Digite o numero que você quer jogar: "))
            from random import randint

            numero_aleatorio = randint(1, 3)
            print(numero_aleatorio)
            if(numero_jogado > 3 or numero_jogado < 1):
                print("Voce digitou um numero invalido!")

            elif numero_jogado == numero_aleatorio:
                print("O numero foi igual, jogue novamente!")
            elif numero_jogado != numero_aleatorio:
                if numero_jogado == 1 and numero_aleatorio == 2 or numero_jogado == 2 and numero_aleatorio == 3 or numero_jogado == 3 and numero_aleatorio == 1:
                    print("Parabens! Você ganhou")
                elif numero_jogado == 2 and numero_aleatorio == 1 or numero_jogado == 3 and numero_aleatorio == 2 or numero_jogado == 1 and numero_aleatorio == 3:
                    print("Você perdeu!")
            print("Sim (1)    Nao (2)")
            resp = int(input("Quer jogar novamente?: "))
            if resp == 2:
                break

    elif Modo_jogo == 2:
        print("Voce escolheu o modo humano vs humano!")
        while Modo_jogo == 2:
            print("Pedra = 1")
            print("Tesoura = 2")
            print("Papel = 3")
            numero_jogador1 = int(input("Jogador 1: Digite o seu numero: "))
            numero_jogador2 = int(input("Jogador 2: Digite o seu numero: "))
            if(numero_jogador1 > 3 or numero_jogador1 < 1):
                print("O jogador 1 colocou um numero invalido!")
            elif(numero_jogador2 > 3 or numero_jogador2 < 1):
                print("O jogador 2 colocou um numero invalido!")

            elif numero_jogador1 == 1 and numero_jogador2 == 2 or numero_jogador1 == 2 and numero_jogador2 == 3 or numero_jogador1 == 3 and numero_jogador2 ==1:
                print("O jogador 1 venceu!")
                numero_partidas += 1
                vitoria_jogador1 += 1
                porcentagem_jogador1 = vitoria_jogador1 * 100/ numero_partidas
                porcentagem_jogador2 = vitoria_jogador2 * 100 / numero_partidas
                print("A quantidade de partidas é:",numero_partidas,", Porcentagem de vitoria do jogador 1:  ", porcentagem_jogador1,"Porcentagem de vitoria do jogador 2: ", porcentagem_jogador2, ",A quantidade de empates é:",numero_empates)
            elif numero_jogador1 == numero_jogador2:
                print("Empate")
                numero_empates += 1
                numero_partidas += 1
                porcentagem_jogador2 = vitoria_jogador2 * 100 / numero_partidas
                porcentagem_jogador1 = vitoria_jogador1 * 100 / numero_partidas
                print("A quantidade de partidas é:", numero_partidas,", Porcentagem de vitoria do jogador 1: ", porcentagem_jogador1, "Porcentagem de vitoria do jogador 2: ",porcentagem_jogador2, ",A quantidade de empates é:", numero_empates)
            elif numero_jogador2 == 1 and numero_jogador1 == 2 or numero_jogador2 == 2 and numero_jogador1 == 3 or numero_jogador2 == 3 and numero_jogador1 ==1:
                print("O jogador 2 venceu!")
                vitoria_jogador2 += 1
                numero_partidas += 1
                porcentagem_jogador2 = int(vitoria_jogador2 * 100/numero_partidas)
                porcentagem_jogador1 = int(vitoria_jogador1 * 100 / numero_partidas)
                print("A quantidade de partidas é:", numero_partidas,", Porcentagem de vitoria do jogador 1: ", porcentagem_jogador1, "Porcentagem de vitoria do jogador 2: ",porcentagem_jogador2, ", A quantidade de empates é:", numero_empates)
            print("Sim (1)     Nao (2)")
            resp = int(input("Quer jogar novamente?: "))
            if resp == 2:
                break
    elif Modo_jogo == 3:
        print("Voce escolheu o modo computador vs computador!")
        while Modo_jogo == 3:
            print("Pedra = 1")
            print("Tesoura = 2")
            print("Papel = 3")
            from random import randint
            computador1 = randint(1, 3)
            print(computador1)
            computador2 = randint(1, 3)
            print(computador2)
            if computador1 == 1 and computador2 == 2 or computador1 == 2 and computador2 == 3 or computador1 == 3 and computador2 == 1:
                print("O computador 1 venceu!")
            elif computador2 == 1 and computador1 == 2 or computador2 == 2 and computador1 == 3 or computador2 == 3 and computador1 == 1:
                print("O computador 2 venceu!")
            else:
                print("Deu empate!")

            print("Sim (1)   Nao (2)")
            resp = int(input("Quer jogar novamente?: "))
            if resp == 2:
                break
    elif Modo_jogo != 1 or Modo_jogo != 2 or Modo_jogo != 3:
        print("Voce colocou um modo invalido!")

    print("Sim (1)    Nao (2)")
    mudar_modo= int(input("Voce deseja mudar de modo?: "))
    if mudar_modo == 2:
        break

