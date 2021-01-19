# MODULES =====================================

import random
import time
import os

# GLOBAL VARIABLES ============================

Msg = """
=================== TIC-TAC-TOE ====================
    The classic game that we used to play in the 
    last few pages, school desks is rightt here.
----------------------------------------------------
"""

board = """
    :-----------------:
    :  7  |  8  |  9  :
    :-----------------:
    :  4  |  5  |  6  :
    :-----------------:
    :  1  |  2  |  3  :
    :-----------------:
"""

win = ['123','456','789','147','258','369','357','159']

p_move = []
c_move = []
all_move = ['1','2','3','4','5','6','7','8','9']

p_pick = ""
c_pick = ""

# FUNCTIONS ====================================

def reset_all():
    
    global p_move, c_move, all_move
    
    p_move = []
    c_move = []
    all_move = ['1','2','3','4','5','6','7','8','9']

def piece():
    
    global p_pick, c_pick

    while True:
        
        os.system('cls')
        
        print("\nPress 1 for choosing '@'\n    OR    \nPress 2 for choosing '#'.\n")
        
        try:
            pick = int(input("Enter choice(1-2):"))
            assert pick in [1,2]
            break
        except:
            print("\nEnter a valid choice.\n")
        
    if pick == 1:
        p_pick = '@'
        c_pick = '#'
    elif pick == 2:
        p_pick = '#'
        c_pick = '@'
    return pick

def display_board():

    global p_move, p_pick
    global c_move, c_pick
    global board, Msg

    print(Msg)

    for i in board:
        if i in p_move:
            print(p_pick, end = '')
        elif i in c_move:
            print(c_pick, end = '')
        else:
            print(i, end = '')

def p_turn():

    global all_move, p_move

    while True:
        try:
            play = input("\nEnter the position where you want to play your turn.\n>>>")
            assert len(play) == 1 and play in all_move
            break
        except:
            print("\nEnter a valid input.\n")
    
    p_move.append(all_move.pop(all_move.index(play))); p_move.sort()

def check(str1, str2):
    for i in str2:
        str1 = str1.replace(i, '')
    return str1

def thinking():

    global p_move, c_move, all_move, win
    p_move_str = ''.join(p_move)
    c_move_str = ''.join(c_move)
    
    stop, p_win = [], False
    iwin, c_win = [], False

    for i in win:
        x = check(i, p_move_str)
        y = check(i, c_move_str)
        
        if len(x) == 1 and x in all_move:
            stop.append(x)
        elif len(x) == 0:
            p_win = True
        
        if len(y) == 1 and y in all_move:
            iwin.append(y)
        elif len(y) == 0:
            c_win = True
    
    return iwin, stop, p_win, c_win

def c_turn():
    
    global all_move, p_move, c_move

    c_gonna_win, c_gonna_stop, c_lose, c_win = thinking()

    if c_gonna_win != []:
        c_move.append(all_move.pop(all_move.index(c_gonna_win[0]))); c_move.sort()
    elif c_gonna_stop != []:
        c_move.append(all_move.pop(all_move.index(c_gonna_stop[0]))); c_move.sort()
    else:
        c_move.append(all_move.pop(all_move.index(random.choice(all_move)))); c_move.sort()

def game_finish():

    c_gonna_win, c_gonna_stop, p_win, p_lose = thinking()

    if p_win:
        return True
    elif p_lose:
        return False
    elif all_move == []:
        return None
    else:
        return 'progress'

def start():

    reset_all()
    pick = piece()
    game = game_finish()
    
    while True:
        
        time.sleep(0.5); os.system('cls')
        display_board()

        if pick == 1:

            p_turn()
            game = game_finish()
            if game != 'progress':
                break

            time.sleep(0.5); os.system('cls')
            display_board()

            c_turn()
            game = game_finish()
            if game != 'progress':
                break
        
        else:

            c_turn()
            game = game_finish()
            if game != 'progress':
                break

            time.sleep(0.5); os.system('cls')
            display_board()

            p_turn()
            game = game_finish()
            if game != 'progress':
                break
    
    time.sleep(0.5); os.system('cls')
    display_board()

    return game
