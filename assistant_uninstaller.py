import os
import shutil
import time
import pickle
import mysql.connector as sql

"""
This module is responsible for removing the personal assistant resources.
It can be used if you want to reset the program data, or if you want to
correct some installing errors.
"""

# remove mysql database -----------------------------------------
def remove_mysqldb():

    # fetches the mysql login credentials
    with open("community_assistant\\mysqldata.dat", 'rb') as x:
        y = pickle.load(x)
    
    mydb = sql.connect(host = y['host'], user = y['user'], passwd = y['passwd'])
    mycur = mydb.cursor()

    # removing mysql database
    try:
        mycur.execute("DROP DATABASE ASSISTANT")
        mydb.commit()
        mydb.close()
    except:
        pass

# remove folders ------------------------------------------------
def remove_folders():

    #removing associated folders
    shutil.rmtree("users_assistant")
    shutil.rmtree("community_assistant")

# remove the newly installed packages --------------------------
def remove_package():

    os.system("pip uninstall google")
    os.system("pip uninstall youtube-search")

# MAIN #===================================================

os.system('cls')

print("Setting up uninstaller...");time.sleep(1);os.system('cls')

print("Removing database...");time.sleep(1);os.system('cls')
try:
    remove_mysqldb()
except:
    pass

print("Removing associated folders...");time.sleep(1);os.system('cls')
remove_folders()

# asks the user whether to save the installed packages or not
c = input("Do you want to remove packages,\nNOTE: These packages can be used in other programs\nEnter (y/n) >>>").lower()
if c == 'y':
    print("Removing packages...");time.sleep(1);os.system('cls')
    remove_package()
else:
    print("Packages saved.")
os.system('cls')

print("Done..."); time.sleep(2); os.system('cls')