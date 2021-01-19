# Modules ===============================================
import Mastermind
import Guess
import TTT
import RPS
import os
import time
import pickle
import mysql.connector

# GLobal variables =======================================

Help = """
The games feature will provide you company when you
are bored or when you want some fun.

Type: games

This will provide you a list of available games.
"""

Msg = """
============================= GAMEZ ===============================

    Want to pass time? Or do you want to challenge other users?
    Anyhow this is the right place for entertainment consisting
    of few classic games. Hope you enjoy them.
-------------------------------------------------------------------
"""

# mySQL connectivity ----------------------------------------

# fetching mysql login credentials
with open("community_assistant\\" + 'mysqldata.dat', 'rb') as x:
    my = pickle.load(x)

mydb = mysql.connector.connect(host = my['host'], user = my['user'], passwd = my['passwd'], database = my['db'])
mycur = mydb.cursor(buffered = True)

# checks whether the highscore databases exists or not(creates them in this case)
try: # the following statements will create the highscore tables
    mycur.execute("CREATE TABLE MASTERMIND(uid varchar(15) primary key, uname varchar(15), score int(50))")
    mydb.commit()
    mycur.execute("CREATE TABLE GUESS(uid varchar(15) primary key, uname varchar(15), score int(50))")
    mydb.commit()
    mycur.execute("CREATE TABLE TTT(uid varchar(15) primary key, uname varchar(15), score int(50))")
    mydb.commit()
    mycur.execute("CREATE TABLE RPS(uid varchar(15) primary key, uname varchar(15), score int(50))")
    mydb.commit()

except: # incase the tables already exists...
    pass

# FUNCTIONS ==============================================

def game_help(): # ---------------------------------------------------
    # tells the user how to use the 'games' command

    global Help
    print(Help)

def scoreboard(game, cond, uid, uname): # ----------------------------
    # this function will store the points of the respective games played by the user in highscore tables.

    global mycur, mydb

    if game > 4:
        return
    all_games = ['MASTERMIND', 'GUESS', 'TTT', 'RPS']
    table_name = all_games[game-1]

    if uid == 'Guest' and uname == 'Guest':
        print("Guest scores are not saved.")

    else:
        # the following set of statements will insert or update the highscore table.

        if cond == True:
            try:
                sqlcmd = "INSERT INTO " + table_name + " VALUES('{}', '{}', {})"
                mycur.execute(sqlcmd.format(uid, uname, 1))
            except:
                sqlcmd = "UPDATE " + table_name + " SET SCORE = SCORE + 1 WHERE uid = '{}'"
                mycur.execute(sqlcmd.format(uid))
        
        elif cond == False:
            try:
                sqlcmd = "INSERT INTO " + table_name + " VALUES('{}', '{}', {})"
                mycur.execute(sqlcmd.format(uid, uname, -1))
            except:
                sqlcmd = "UPDATE " + table_name + " SET SCORE = SCORE - 1 WHERE uid = '{}'"
                mycur.execute(sqlcmd.format(uid))
        
        elif cond == None:
            pass
    
    mydb.commit()

def show_leaderboards(game_name): # ---------------------------------------------------
    # this is responsible for displaying the highscore to the user.
    # where's the fun if the player is not able to see his/her score anyway XD
    
    global mydb, mycur

    print()
    print(game_name)
    print()

    # the sql command to be executed
    sqlcmd = "SELECT * FROM " + game_name + " ORDER BY SCORE DESC"

    mycur.execute(sqlcmd) # execution
    table = mycur.fetchall()
    
    if table == []: # in case there is no record of scores, message is displayed
        print("No data available.")
        return

    # the following segment is made to display the highscore table in a good format
    
    fields = 'Sno' +' | '+ '         UserID' +' | '+  '       UserName' +' | '+  'Score'
    print(fields)

    # separation line between field names and records
    divider = ''
    for i in range(len(fields)):
        divider += '-'
    print(divider)
    
    spacer = '               ' # just a variable which is used to align the columns

    # this loop is aligning the records so that there is no inconsistency in the displayed table
    for i in range(len(table)):
        n = i+1

        sno = spacer[0:3-len(str(n))] + str(n)
        userid = spacer[0:15-len(table[i][0])] + table[i][0]
        uname = spacer[0:15-len(table[i][1])] + table[i][1]
        score = spacer[0:5-len(str(table[i][2]))] + str(table[i][2])

        row = sno +' | '+ userid +' | '+ uname +' | '+ score
        print(row)
    
    print()

# the function that is implemented in the program ------------------------------

def games(uid, uname): # uid, uname are parameters to know which user is interacting.
    # this function provides a interaction method with the user.
    
    global Msg

    # the loop to display options to user and handle input errors simultaneously
    while True:
        os.system('cls')
        print(Msg)
        print()
        print("Which game do you want to play?")
        print("(1) Mastermind")
        print("(2) Word-Guessing")
        print("(3) Tic-tac-toe")
        print("(4) Rock-Paper-Scissors")
        print("(5) Leaderboard")
        print("(6) Back")

        try:
            c = int(input("Enter choice(1-6):"))
            assert c in range(1,7)
            
            if c == 1:
                time.sleep(1); os.system('cls')
                x = Mastermind.start(); print("\nGAME OVER") # starts mastermind game
            
            elif c == 2:
                time.sleep(1); os.system('cls')
                x = Guess.start(); print("\nGAME OVER") # starts word guessing game
            
            elif c == 3:
                time.sleep(1); os.system('cls')
                x = TTT.start(); print("\nGAME OVER") # starts tic tac toe
            
            elif c == 4:
                time.sleep(1); os.system('cls')
                x = RPS.rps(); print("\nGAME OVER") # starts the rock paper scissors game
            
            elif c == 5: # to show the scoreboard
                x = None
                try:
                    name = int(input("\nEnter Game number(1-4):"))
                    assert name in range(1, 5)
                    g = [0, 'Mastermind', 'Guess', 'TTT', 'RPS']
                    show_leaderboards(g[name])
                except:
                    print("That's not a valid input. Check the game number !")

            elif c == 6:
                break
            
            else:
                print("Enter a valid choice.")

            # when the game ends, True, False or None output is played
            # True - user won the game
            # False - user lost the game
            # None - the game was a draw
            scoreboard(c, x, uid, uname) # the function updates the score table.

            input("\nPress ENTER\n")

        except:
            print("Enter a valid input.")
            time.sleep(1)
            
