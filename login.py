import pickle
import os
import mysql.connector as sql
import time
import shutil

# connects with the mysql database to fetch account details
with open("community_assistant\\" + 'mysqldata.dat', 'rb') as x:
    my = pickle.load(x)

mydb = sql.connect(host = my['host'], user = my['user'], passwd = my['passwd'], database = my['db'])
mycur = mydb.cursor()

try:
    mycur.execute("CREATE TABLE ACCOUNTS(uid varchar(15) primary key, uname varchar(15), pwd varchar(50))")
    mydb.commit()
    mycur.execute("INSERT INTO ACCOUNTS VALUES('guest', 'guest', 'guest')")
    mydb.commit()
except:
    pass

# ACCOUNT CREATION FUNCTIONS ===================================

def pwd(): # ----------------------------------------------------------------------
    # used in case of password creation.
    # returns a string which is a password.

    while True:
        time.sleep(1);os.system('cls')
        print("PASSWORD=================================\n")
        x = input("Create password:")
        y = input("Re-enter password:")

        # this segment checks the strength of the password.
        if len(x) < 8:
            print('Enter atleast 8 characters for password.')
            continue

        s = [0,0,0] # it is a metre to measure the strength of password.

        for i in x:
            if i.isdigit():
                s[0] += 1
            elif i.isupper():
                s[1] += 1
            elif not i.isalpha():
                s[2] += 1
        
        if s.count(0) > 1: # when the entered password fails the strength test
            print("Password is weak.")
            print("Include special characters, digits or uppercase.")
            continue
        
        if x != y:
            print("Re-entered password doesn't match the password.")
            continue
        break
    
    time.sleep(1);os.system('cls')
    return x

def signup(): # ------------------------------------------------------------------------
    # this function is executed when a user creates a new account.
    # at the most basic level, UID, UNAME, PASSWORD is created.
    # user related items like folders, binary files, sql record are created.
    # major portion is used in handling errors.

    global mydb, mycur

    while True:

        time.sleep(1);os.system('cls')

        # sometimes, the user may accidently choose the create account option.
        # to cancel the process, he/she may quit by leaving the entries empty.
        print("Incase you don't want to create an account,")
        print("then leave the entry empty and press ENTER.")
        
        print("USERID================================\n")
        uid = input("Enter UserID:") # userid is created

        if len(uid) == 0: # the process cancellation condition
            print("Account not created.")
            time.sleep(1);os.system('cls')
            return None

        # the try block checks whether a user id is unique or not.
        try:
            mycur.execute("SELECT * FROM ACCOUNTS WHERE uid = '{}'".format(uid))
            l = mycur.fetchone()
            if l != None:
                assert len(l) == 3
        except:
            print('UserID is not unique. Try another ID.')
            continue
        break

    time.sleep(1);os.system('cls')
    
    # USERNAME ------------------------------------------------------
    
    print("USERNAME===================================\n")
    uname = input("Enter Username:")

    passwd = pwd() # password input

    # new user data is entered in the accounts table
    
    mycur.execute("INSERT INTO ACCOUNTS VALUES('{}', '{}', '{}')".format(uid, uname, passwd))
    mydb.commit()

    # creates the assosciated items for the user data storage.
    
    fh = open('users_assistant\\' + uid + '.dat', 'wb')
    pickle.dump({'notification':[], 'reminder':[]}, fh)
    fh.close()

    os.mkdir('users_assistant\\' + uid)
    fh = open('users_assistant\\' + uid + '\\mynotes.txt', 'w')
    fh.close()

    # message to the user.
    
    print('Account created successfully.')
    time.sleep(1);os.system('cls')

def login(): # ---------------------------------------------------------------
    # this function is used when user is logging in to use the features.

    global mydb, mycur

    time.sleep(1); os.system("cls")

    print("LOG-IN======================================\n")
    uid = input('Enter UserID:')
    passwd = input("Enter password:")

    # the segment is executed to cross check the login credentials with the user database.

    mycur.execute("SELECT * FROM ACCOUNTS WHERE uid = '{}' AND pwd = '{}'".format(uid, passwd))
    
    tup = mycur.fetchone()
    if tup != None:
        if len(tup) == 3:
            print("Log-in successful.")
            time.sleep(1);os.system('cls')
            return tup
    else: # when the entries don't match the user database, login fails and message is displayed.
        print("Incorrect UserID or Password.")
        print("You may create a new account if you are new.")    
    
    time.sleep(1);os.system('cls')

# ACCOUNT MANAGEMENT FUNCTIONS =================================================

def Help(x): # ---------------------------------------------------------------
    # this function tells user the use and purpose of the login commands.

    if x == "unamecng":
        print("This command will allow you to change your username.")
    elif x == "pwdcng":
        print("This command will allow you to change your password.")
    elif x == "delete":
        print("This command will delete your account.")
    elif x == "account":
        print("This command will show you your account details.")
    elif x == "logout":
        print("Don't panic, this will just log you out of the session.")

def account_details(uid): # -----------------------------------------------------
    # shows user the account details

    # fetches the data from the mysql database
    mycur.execute("SELECT * FROM ACCOUNTS WHERE uid = '{}'".format(uid))
    ac = mycur.fetchone()
    user = ac[0]
    uname = ac[1]

    # printing the output
    print("User Details =====================\n")
    print("UID:", user)
    print("UName:", uname)
    print("\nPress ENTER to continue\n")
    input("")
    time.sleep(1);os.system('cls')

def change_pwd(uid): # ----------------------------------------------------------
    # it allows user to change their password.

    mycur.execute("SELECT * FROM ACCOUNTS WHERE uid = '{}'".format(uid))
    ac = mycur.fetchone()
    user = ac[0]
    uname = ac[1]
    passwd = ac[2]

    # this segment first verifies whether the real user is changing the password.
    print("Password Change ======================\n")
    i = input("Enter Old password:")
    if i != passwd: # if the old password is incorrect, then the password change is denied.
        print("Password does not match.")
    
    else:
        f = pwd() # new password creation.
        mycur.execute("UPDATE ACCOUNTS SET pwd = '{}' WHERE uid = '{}'".format(f, user)) # table is updated.
        mydb.commit()
        print("Password changed.")
    
    time.sleep(1);os.system('cls')

def change_uname(uid): # ---------------------------------------------------
    # this is a function just to change the username that is displayed in the welcome screen.

    global mydb, mycur

    print("Username change ==========================\n")

    # this message is covering the sql attribute entry length of username
    print("Note: If you username is too long, the username will not be changed.\n")
    
    name = input("Enter new username:") # new username input.
    
    mycur.execute("UPDATE ACCOUNTS SET uname = '{}' WHERE uid = '{}'".format(name, uid))
    mydb.commit()

    print("Username changed.") # message to the user.

    time.sleep(1);os.system('cls')

def delete_account(uid): # ---------------------------------------------------------
    # this function will delete the user account.

    global mydb, mycur

    while True:
        
        time.sleep(1);os.system('cls')
        print("Account Deletion ======================================\n")
        
        try:
            # final confirmation enquiry
            x = input("Are you sure you want to delete this account(y/n):").lower()
            assert x in ['y', 'n']

            if x == 'y':
                mycur.execute("DELETE FROM ACCOUNTS WHERE uid = '{}'".format(uid))
                mydb.commit()
                
                # removing the user associated folders.
                os.remove("users_assistant\\" + uid + ".dat")
                shutil.rmtree("users_assistant\\" + uid)
                print("Account deleted.") # account deletion message.
            
            else: # message to user when account not deleted.
                print("Account not deleted.")

        except: # execption handling.
            print("Enter a choice as either 'y' or 'n'.")
            continue

        break
