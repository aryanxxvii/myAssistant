import googlesearch
import youtube_search
import webbrowser

# GLOBAL VARIABLE ================================================

Help = """
The search feature will fetch results from the internet.
For this, internet connection should be available.

To execute a search, type:

search [x] [Query]

Here, the parameter 'x' has two options:
g - Search through google
y - Search through youtube
"""

# display help -------------------------------------------------
def search_help():
    # tells the user the way to use the command.
    global Help
    print(Help)

# perform youtube serach ---------------------------------------
def search_youtube(query): # query parameter takes the search input.

    # uses the youtube_search module to fetch the youtube results of the query in form of dictionary.
    Results = youtube_search.YoutubeSearch(query, max_results = 5).to_dict()
    results = [] # empty list where the fetched results are organised.
    
    for i in range(len(Results)):
        # looping through the Results dictionary to filter the neccessary data.

        d = {'title': Results[i]['title'], 
        'channel': Results[i]['channel'], 
        'duration': Results[i]['duration'], 
        'views': Results[i]['views'], 
        'url': 'https://www.youtube.com' + Results[i]['url_suffix']}

        results.append(d)

    # gives back a list.
    return results

# perform google search ---------------------------------------
def search_google(query): # query paramater takes the search input.
    
    results = [] # empty list where the fetched results are organised.

    # uses the googlesearch module to fetch results.
    for i in googlesearch.search(query, tld="co.in", num=10, stop=10, pause=2):
        results.append(i)

    # gives bacck a list of various links.
    return results

# output to user -----------------------------------------------
def get_results(query, x = 'g'):
    # this function is being implemented that uses the above 2 functions.
    # the  new parameter determines which function is to be used and accordingly, results are displayed.

    # this part is getting the list of search results and display it to user.
    print("SEARCH RESULTS ===========================\n\n")

    if x == 'y':
        r = search_youtube(query)
        for i in range(len(r)):
            print('('+str(i+1)+')', r[i]['title'], '\t', '---', '\t', r[i]['channel'])
            print('['+r[i]['duration']+']', '\t\t', '['+r[i]['views']+']')
            print(r[i]['url'])
            print('\n\n')
    
    elif x == 'g':
        r = search_google(query)
        for i in range(len(r)):
            print('('+str(i+1)+')', r[i])
            print('\n')
    
    print("If you want to open the link, enter the corresponding link number.")
    print("Otherwise you can enter 'n'.\n")

    # the following part uses the webbrowser module to open the desired link after taking input.
    while True:

        # try, except block to handle user input errors.
        try:
            n = (input("Enter response:")).lower()

            if n == 'n':
                pass
            
            else:
                n = int(n)-1
                assert n in range(len(r))

                if x == 'y':
                    webbrowser.open(r[n]['url'])
                elif x == 'g':
                    webbrowser.open(r[n])
        
        except:
            print("Enter a valid input.\n")
            continue

        break
