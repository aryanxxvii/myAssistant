import pickle
import datetime
import tkinter

"""
This module is working behind the scenes and manages the notifications of the user.
The user is not aware that it is working. It is responsible for reminder pop-ups
when the time comes.
"""

# pop-up ---------------------------------------------------
def pop_up(x, uid):
    # uses the tkinter modulle to display a notifivation pop-up.
    # dedicated to GUI of the notification. (no processing)
    
    root = tkinter.Tk()
    root.title("Notification! for - " + uid)
    tkinter.Label(root, text = x, fg = 'white', bg = 'black', width = 100, height = 10).pack()
    tkinter.Button(root, text = 'OK', command = root.destroy, width = 10).pack()
    tkinter.mainloop()

# checks notification --------------------------------------
def notifications(uid): # uid parameter is needed to know which user is to active.
    # the function is responsible for shifting the reminders to notification bar when time arrives.

    # opens the user's binary file.
    with open("users_assistant\\" + uid + ".dat", 'rb') as file:
        x = pickle.load(file)

    # shifting process.
    i = 0
    while i < len(x['reminder']):
        if x['reminder'][i][0] <= datetime.datetime.now():
            print(type(x['reminder'][i][0]))
            x['notification'].append(x['reminder'].pop(i))
        else:
            i += 1

    # changes are stored in the same file.
    with open("users_assistant\\" + uid + ".dat", 'wb') as file:
        pickle.dump(x, file)

# notify ------------------------------------------------------
def notify(uid):
    # this function is responsible fot displaying any message in the notification bar.
    # uses the pop-up function for a popup.

    # opening binary file and loops through the notification bar.
    # once, the user is notified, that notification is deleted from the notification bar.
    with open("users_assistant\\" + uid + ".dat", 'rb') as file:
        x = pickle.load(file)

    while len(x['notification']) != 0:
        i = x['notification']
        time = str(i[0][0])
        msg = i[0][1]
        i.pop()
        pop_up(time + '\n' + msg, uid)

    # changes are stored.
    with open("users_assistant\\" + uid + ".dat", 'wb') as file:
        pickle.dump(x, file)
