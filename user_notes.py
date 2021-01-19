import os

Help = """
You can write notes, todo lists etc. for yourself here.
Use 'DELETE ALL' to reset your notes.
Press ENTER to finish writing.
"""

def user_notes_help():
    global Help
    print(Help)

def start_notes(uid, Text_file = '\\mynotes.txt', x = 'myNOTES'):

    note = ' '
    while note != '':
        
        os.system('cls'); print(x)
        
        try:
            read_user_notes(uid, Text_file)
        except:
            pass
        
        note = write_user_notes(uid, Text_file)
        
        if note == "DELETE ALL":
            delete_notes(uid, Text_file)

def write_user_notes(uid, Text_file = '\\mynotes.txt'):

    note = input("What's on your mind?: \n>>> ")

    fh = open("users_assistant\\" + uid + Text_file, 'a')
    if note != '':
        fh.write(note +'\n')
    else:
        pass
    fh.close()

    return note
    
def read_user_notes(uid, Text_file = '\\mynotes.txt'):

    fh = open("users_assistant\\" + uid + Text_file, 'r')

    for line in fh:
        print('> ', line)
    fh.close()

def delete_notes(uid, Text_file = '\\mynotes.txt'):
    
    fh = open("users_assistant\\" + uid + Text_file, 'w')
    fh.write('')
    fh.close()