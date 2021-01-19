import datetime
import pickle

# GLOBAL VARIABLE ========================================================

Help = """
The reminder feature will take time, date along with the message
to remind you about the things which you don't want to forget.

To set a reminder, type:

remind at [hh:mm] on [DD-MM-YYYY] that [Your Message]

For quick setting,
1. Use the 'now' keyword to set the current time, or date.
2. If you don't specify parameter, it will be set as 'now'.
3. If you want a reminder after few minutes, type the time as
    +minutes format.
    
    Eg: remind after +5.... (reminds you after 5 minutes.)
"""

# display help -----------------------------------------------------------
def reminder_help():
    # this function explains user on how to use the command.

    global Help
    print(Help)

# set datetime -----------------------------------------------------------
def set_datetime(time, date):
    # input parameters are string format.
    # this function checks the input format of date and time.
    # if the format is correct, the input is converted into datetime object.
    
    if '+' in time:
        try:
            time = int(time[1:])
            rem = datetime.datetime.now() + datetime.timedelta(minutes = time)
        except:
            print("Enter the time in integer format after the '+' sign.")
            rem = None

    else:
        if time == 'now':
            time = datetime.datetime.now().strftime("%H:%M")
        if date == 'now':
            date = datetime.datetime.now().strftime("%d-%m-%Y")
        
        try:
            rem = datetime.datetime.strptime(time + ' ' + date, "%H:%M %d-%m-%Y")
        except:
            print("The specified time or date format not does match the given.")
            rem = None

    # datetime object is returned.
    return rem

# set reminder -----------------------------------------------------------
def set_reminder(uid, msg = "Reminder", time = 'now', date = 'now'):
    # this function stores the reminder in user's binary file.
    # format: [datetime object, message]

    rem = set_datetime(time, date) # gives us the datetime object.

    # in case error occurs in the above statement, appropriate message is displayed and we return.
    if rem == None:
        return

    # this segment stores the reminder in the binary file.    
    else:
        with open("users_assistant\\" + uid + ".dat", 'rb') as file:
            x = pickle.load(file)
        
        x['reminder'].append([rem, msg])

        with open("users_assistant\\" + uid + ".dat", 'wb') as file:
            pickle.dump(x, file)

    print("Reminder set.") # display message to tell user that the reminder is set.

# input function ---------------------------------------------------------
def reminder_input(uid, qry):
    # this function is extracting the details from the structured input.
    # it the the function that is being implemented in the program.

    if qry[1] == 'at' and qry[3] == 'on':
        set_reminder(uid, ' '.join(qry[5:]), qry[2], qry[4])
    elif qry[1] == 'at':
        set_reminder(uid, ' '.join(qry[3:]), time = qry[2])
    elif qry[1] == 'on':
        set_reminder(uid, ' '.join(qry[3:]), date = qry[2])
    elif qry[1] == 'after':
        set_reminder(uid, ' '.join(qry[3:]), time = qry[2])
    
    else:
        # appropriate message when the input format is wrong.
        print("Format is not matching. Use Help to know more.")
