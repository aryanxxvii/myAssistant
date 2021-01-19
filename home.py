import os
import time
import pickle
import datetime
import login
import search
import reminder
import notifications
import notes
import games
import user_notes
import my_calendar

"""
This is the actual interface for the user which uses all the modules needed.
The interface is based on a structured inputs given by the user. The user
can use the help feature to know the use of commands.
"""

commands = ['remind', 'search', 'games', 'logout', 'delete', 'unamecng', 'pwdcng', 'account', '?makenotes', 'mynotes', 'mycalendar']

uid = None
uname = None

def welcome_message(uid = None, uname = None):

    print("\n===========================================WELCOME============================================\n")
    
    print("     Use this personal assistant to keep record of your tasks, set reminders, play minigames    ")
    print("                 and much more. Sign-up to gain access more features.                           ")
    print("")
    print("UserID:", uid)
    print("Username:", uname)
    print("")
    print("\t\t\t                               Today:", datetime.datetime.today().strftime("%d-%B-%Y , %A"))
    
    print("\n----------------------------------------------------------------------------------------------\n")

def Help():
    
    global commands

    print('You may type help [command_name] to know more.')
    print('List of commands:')
    for i in range(len(commands)):
        print(str(i+1) + '.', commands[i])

def query():

    global commands
    global uid
    global uname
    
    print('\nPress ENTER occasionally to refresh the screen.\nType help for information.\n')
    qry = input("Write:").lower().split()
    print()

    try:

        if qry[0] == 'help' and len(qry) > 1:
            
            if qry[1] in commands:
                if qry[1] == commands[0]:
                    reminder.reminder_help()
                elif qry[1] == commands[1]:
                    search.search_help()
                elif qry[1] == commands[2]:
                    games.game_help()
                elif qry[1] == commands[3]:
                    login.Help(qry[1])
                elif qry[1] == commands[4]:
                    login.Help(qry[1])
                elif qry[1] == commands[5]:
                    login.Help(qry[1])
                elif qry[1] == commands[6]:
                    login.Help(qry[1])
                elif qry[1] == commands[7]:
                    login.Help(qry[1])
                elif qry[1] == commands[8]:
                    notes.notes_help()
                elif qry[1] == commands[9]:
                    user_notes.user_notes_help()
                elif qry[1] == commands[10]:
                    my_calendar.my_calendar_help()

        elif qry[0] == 'help':
            Help()
        
        elif qry[0] == 'remind':

            if uid == 'Guest':
                print("Guest can't set reminders.")
            
            else:
                reminder.reminder_input(uid, qry)
        
        elif qry[0] == 'search':

            if qry[1] in ['g', 'y']:
                search.get_results(' '.join(qry[2:]), qry[1])
            else:
                search.get_results(' '.join(qry[1:]))

        elif qry[0] == 'games':
            games.games(uid, uname)
    
        elif qry[0] == 'logout':

            uid = None
            uname = None
        
        elif qry[0] == 'delete':
            if uid != 'Guest':
                login.delete_account(uid)
        
        elif qry[0] == 'pwdcng':
            if uid != 'Guest':
                login.change_pwd(uid)
        
        elif qry[0] == 'unamecng':
            if uid != 'Guest':
                login.change_uname(uid)
        
        elif qry[0] == 'account':
            login.account_details(uid)

        elif qry[-1] == '?makenotes':
            if len(qry) > 1:
                notes.makenotes(' '.join(qry[:-1]))
            else:
                print("You need to enter some lines to make notes on.")
        
        elif qry[0] == 'mynotes':
            if uid == 'Guest':
                print("Guests can't use this feature")
            else:
                user_notes.start_notes(uid)
            
        elif qry[0] == 'mycalendar':
            if uid == 'Guest':
                print("Guest can't set reminders.")
            
            else:
                my_calendar.start(uid)
        
        else:
            pass

    except:
        pass

# Main Program

while True:

    input("\nPress ENTER\n"); os.system('cls')
    
    if uid not in [None, 'Guest']:
        notifications.notifications(uid)
        notifications.notify(uid)

    welcome_message(uid, uname)

    if uid == None and uname == None:

        options = ['Login', 'Create Account', 'Guest', 'Quit']

        for i in options:
            print(options.index(i)+1, i)
        
        print("If you are a guest, most of the features will not work.\n")
        
        while True:
            try:
                choice = int(input('Enter choice(1-4):'))

                if choice == 1:
                    user = login.login()
                    if user != None:
                        uid = user[0]
                        uname = user[1]
                    break

                elif choice == 2:
                    login.signup()
                    break

                elif choice == 3:
                    uid = uname = 'Guest'
                    break

                elif choice == 4:
                    mydb.close()
                    exit()

                else:
                    print('Enter a valid choice.') 

            except:
                print("Enter a valid choice.")
                continue

    else:
        query()
