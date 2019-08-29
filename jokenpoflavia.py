from random import randint
from time import sleep


listaopts = ["Explosão Nuclear", "Barata", "Pé"]

computador = randint (0,2)

partida = 1
ganhou = 0 

print ("Esse jogo é similar ao JOKENPO tradicional com Pedra, Papel e Tesoura. Mas um pouquinho diferente! \n")
print ("Aqui vamos utilizar 3 parâmetros: Barata, pé ou Explosão! E adivinha? \n")
print ("A explosão nuclear não mata a barata, mas a barata é esmagada pelo pé, que morre na explosão nuclear!")

PergJogador = 3

while PergJogador != 0 and PergJogador != 1 and PergJogador != 2:
    PergJogador = int(input('''Escolha uma opção para lutar:" 

    [0] Explosão
    [1] Barata
    [2] Pé
   
    Digite sua escolha:''' ))

    if PergJogador != 0 and PergJogador != 1 and PergJogador != 2:
        print("Escolha uma opção válida")
    else: 
        print("\nOLHA\n")
        sleep(1)
        print("A\n")
        sleep(1)
        print("EXPLOSÃO!\n")
        sleep(1)

        print ("x-"*20)
        print ("Seu adversário escolheu: %s" % (listaopts[computador]))
        print ("Sua escolha foi: %s" % (listaopts[PergJogador]))
        print ("x-"*20)
        print ("\n")



        if computador == 0: 
            if PergJogador == 0:
                print ("Empatou, zé ruela!")
            elif PergJogador == 1:
                ganhou += 1
                print ("BOOM. Aparentemente você ganhou, pois a barata (infelizmente) sobrevive a explosão nuclear.")
            elif PergJogador == 2:
                print ("Oops, você morreu e o seu pé foi explodido.")
            else:
                print ("Aparentemente você digitou algo errado, tente novamente.")

        if computador == 1:
            if PergJogador == 0:
                print ("Você perdeu. A barataGamer sobreviveu a sua tentativa de explodi-la!! =^.^= ")
            elif PergJogador == 1:
                print ("Barata com Barata dá? EMPATE!")
            elif PergJogador == 2:
                ganhou += 1
                print ("SMASH. Parabéns, você esmagou a barata com o seu pezin! THAT'S A JOB WELL DONE!")
            else: 
                print ("Aparentemente você digitou algo errado, tente novamente.")

        if computador == 2:
            if PergJogador == 0:
                ganhou +=1
                print ("BOOM CAPAKFKA!!!!! PARABÉNS. Você ganhou e explodiu o pé do adversário! :D")
            elif PergJogador == 1:
                print ("UPS. Você foi esmagado pelo pé de pixels, coleguinha! ): Tenta de novo.")
            elif PergJogador == 2:
                print ("PÉ com PÉ... 2 pés. É, parece razoável, mas não foi dessa vez. EMPATOU!")
            else:
                print ("Aparentemente você digitou algo errado, tente novamente.")

        PergJogador = 3

        tryagain =  (input ("Você gostaria de jogar novamente? s para SIM ou n para NÃO"))

        if tryagain == 's':
            partida += 1
        else:
            print ("Você jogous %d partidas e ganhou %d." % (partida, ganhou))
            break

        


 



