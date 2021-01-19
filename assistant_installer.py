import os
import pip
import mysql.connector as sql
import pickle
import time

'''
This module is responsible for setting up the personal assistant resources.
The actual file will show error if used directly.
So, it is advised to run this module to initialise the assistant.
'''

# folder setup ------------------------------------------
def folder_setup():
    #setting up folder where the user data is permanently stored.
    os.mkdir("users_assistant")
    os.mkdir("community_assistant")

# storage setup ----------------------------------------
def storage_setup():
    #setting up storage files within the created folder.

    binary_files = ["mysqldata.dat", "commcentre.dat"]
    
    fh1 = open("community_assistant\\" + binary_files[0], 'wb')
    fh1.close()
    
    fh2 = open("community_assistant\\" + binary_files[1], 'wb')
    fh2.close()

# mysql setup ------------------------------------------
def mysql_setup():
    # creates the mysql database related to the program
    
    # creating a binary file to store the mysql data as it is different for different systems, users.
    # here, error is not handled, so it is mandatory to enter the correct credentials.
    with open("community_assistant\\" + "mysqldata.dat", 'wb') as x:

        Host = input("Enter MySQL host name:")
        User = input("Enter MySQL user name:")
        Pass = input("Enter MySQL pass-word:")
        MyDB = "Assistant" # the database associated with the program

        Dump = {'host': Host, 'user':User, 'passwd':Pass, 'db':MyDB}
        pickle.dump(Dump, x)
    
    mydb = sql.connect(host = Host, user = User, passwd = Pass)
    mycursor = mydb.cursor()

    # this part is little sensitive, in case database assistant already exists, it clears all its tables.
    # in case, you already have important database assistant, then its data will be removed.
    try:
        mycursor.execute("DROP DATABASE {}".format(MyDB))
    except:
        pass

    mycursor.execute("CREATE DATABASE {}".format(MyDB))
    mydb.commit()
    mydb.close()

# package setup ------------------------------------------------
def package_setup():
    # this function installs the python modules(other than the in-built ones) that are used in the program
    os.system("pip install google") # used in search module
    os.system("pip install youtube-search-python") # used in search module
    os.system('cls')

# MAIN #=======================================================

os.system('cls')

print('Setting up folder...'); time.sleep(1); os.system('cls')
folder_setup()

print("Setting up storage resources..."); time.sleep(1); os.system('cls')
storage_setup()

print("Setting up mysql database..."); time.sleep(1); os.system('cls')
mysql_setup()

print('Fetching required packages...'); time.sleep(1); os.system('cls')
package_setup()

os.system('cls')

print("Done..."); time.sleep(2); os.system('cls')
