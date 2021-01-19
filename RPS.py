from random import randint
import time
import os

def rps():

    while True:
        try:
            _time_ = int(input("Best of : "))
            os.system("cls")
            break
        except:
            print("Enter an integer.")


    t = ["Rock", "Paper", "Scissors"]

    #assign a random play to the computer

    score_p = 0

    score_c = 0

    while score_p + score_c < _time_:
        
        time.sleep(2)
        os.system("cls")
        print("YOU: ",score_p,'\n'+"COM: ",score_c,'\n')
        
        computer = t[randint(0,2)].upper()
        i = 1
        while i == 1:
            player = (input("Rock, Paper or Scissors? ")).upper()
            if player == 'ROCK' or player == 'SCISSORS' or player == 'PAPER':
                i = 0
            else:
                print("INVALID INPUT")
                i = 1
        
            
                
        
        print("\nCOMPUTER CHOSE: ", computer,'\n')

        if player == computer:
            print("Tie!")
            

        elif player == 'ROCK':
            if computer == 'PAPER':
                print("YOU LOSE")
                
                score_c += 1
                
            else:
                print("YOU WON!")

                score_p += 1
            

        elif player == 'SCISSORS':
            if computer == 'ROCK':
                print("YOU LOSE")
                
                score_c += 1

            else:
                print("YOU WON!")
                
                score_p += 1
            
            
                
        elif player == 'PAPER':
            if computer == 'SCISSORS':
                print("YOU LOSE")
                
                score_c += 1

            else:
                print("YOU WON!")

                score_p += 1
            


        else:
            print("That's not a valid input. Check your spelling!")


    if score_p > score_c:
        print("\n\n==YOU WON THE GAME!== \n")
        print("The final score is: \n", "YOU-",score_p,"\n", "COMPUTER-", score_c)
        return True
            
    else:
        print("\n\n==YOU LOST THE GAME== \n")
        print("The final score is: \n", "YOU-",score_p,"\n", "COMPUTER-", score_c)
        return False