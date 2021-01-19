import reminder
import user_notes
import calendar
import datetime
import os

Help = """
Make your planning more efficient with the use of calendar.
You won't miss your favourite events like watching movies,
plan tours, mark birthdays, manage datewise to-do lists and
other benefits by using it in the best possible way.
"""

Msg = """
======================== Welcome to Calendar ============================

    Were you ever confused what all things you need to do and you
    are not able to focus? Did you ever forget some important events?
    Have you experienced the power of proper planning? Have you ever
    felt the need to plan things out?....

    Reminder:
    " A goal without a plan is just a wish. "
                                 -- Antoine de Saint-Exupery 
-------------------------------------------------------------------------
"""

def my_calendar_help(): # -----------------------------------------------
    # tells the user about how to use the feature.

    global Help
    print(Help)

def display_calendar(year): # -------------------------------------------
    # displays the calendar of a particular year using the calendar module.

    x = calendar.calendar(year)
    print(x)

def display_month(year, month): # ---------------------------------------
    # display the calendar of a particular month of the year.

    x = calendar.month(year, month)
    print(x)

def start(uid): # --------------------------------------------------------
    # the actual command implemented in the program
    # the uid parameter is used to know which user is wanting to use the feature.

    # the special thing is that the user is able to create to-do lists for a particular date.

    global Msg

    try:
        os.system('cls'); print(Msg)
        
        # input for the year
        yys = input("Enter Year(YYYY):")
        assert len(yys) == 4
        yy = int(yys)
        
        os.system('cls'); print(Msg)
        display_calendar(yy)

        # input for the month
        mms = input("Enter Month number(MM):")
        assert len(mms) == 2
        mm = int(mms)
        
        os.system('cls'); print(Msg)
        display_month(yy, mm)

        print("If you want to add notes for a particular date,")
        print("or read the notes you have added for that day then")
        print("you may enter the respective date and review the notes.")
        print("Otherwise you may just press ENTER to ignore.")
        print()
        dd = input("Enter Date(DD):")
        assert len(dd) == 2 and uid != 'Guest'

        Date = dd + '-' + mms + '-' + yys # formatting the date structure for input parameter.

        # sets the reminder to notify user that he/she has made plans for that day.
        reminder.set_reminder(uid, "Calendar notification. Check calendar.", time = '06:00', date = Date)

        # storing the to-do list plans in a text file.
        user_notes.start_notes(uid, '\\'+Date, Msg)
    
    except:
        pass
