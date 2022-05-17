def jogo_adivinhacao():
    import random

    print("********************************")
    print("Bem vindo ao Jogo de adivinhacao")
    print("********************************")

    numero_secreto = (random.randrange(1, 101)) #O random gera um numero de 0.0 ate 1.0, entao precisa do randrange q ele limita ja que nao quero o numero 0
    total_tentativas= 0
    pontos = 1000
#Seleção de dificuldade
    print("Qual nivel de dificuldade voce quer?")
    print("(1) Facil (2) Medio (3) Dificil")
    nivel = int(input("Defina um Nível: "))
#Definição de quantas tentativas cada dificuldade tem
    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("tentativa {} de {}". format(rodada,total_tentativas))
    #Parte do chute
        chute_str =input("Digite o seu numero entre 1 e 100: ")
        chute = int(chute_str)
        print("Voce digitou", chute)
    #Caso o jogador digite um numero invalido
        if (chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 e 100!")
            continue
    #Definindo variaveis para facilitar o codigo
        acertou = numero_secreto == chute
        maior  = chute > numero_secreto
        menor = chute < numero_secreto
    #Caso acerte
        if (acertou):
            print("Voce acertou!")
            print("Voce fez {}!". format(pontos))
            break #break deixa de rodar quando isto acontece

        else:
            if (maior):
                print("Seu chute foi maior do que o numero secreto")
                if (rodada == total_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif (menor):
                print("Seu chute foi menor do que o numero secreto")
                if (rodada == total_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute) #Exemplo: 40 - 20 = 20 pontos perdidos
            pontos = pontos - pontos_perdidos

    print("Fim de jogo")

#For = coloca com qual valor voce quer começar e dps o qual voce quer chegar
#range define a serie de valores EXEMPLO: for rodada in range(1,10): vai imprimir 1 ate 9, pois o 10 é exclusiva e o range termina
#Em um nao-exclusivo
#range(start, stop, [step] codigo do range
if(__name__ == "__main__"):
    jogo_adivinhacao()