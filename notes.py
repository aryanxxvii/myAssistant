Help = """
This feature will convert long paragraphs into
more convinient and readable form. You can try
it out by typing:

[your long paragraph] ?makenotes
"""


def notes_help(): # ----------------------------------------
    # displays the way to use this feature.

    global Help
    print(Help)

def makenotes(para):

    #INPUT#======================
    para0 = para.split()

    #ORGANISE#===================
    d = dict()
    L = []
    n = 1
    for i in para0:
        if '.' in i or '?' in i or '!' in i:
            L.append(i)
            d[n] = L
            L = []
            n = n+1
        else:
            L.append(i)

    #PRE-DEFINED LIST#===========(basic requirements)
    prep = ['at','aboard', 'about', 'above', 'across',
        'after', 'against', 'along', 'amid', 'among', 'anti', 'around', 'as',
        'before', 'behind', 'below', 'beneath', 'beside', 'besides',
        'between', 'beyond', 'by', 'concerning', 'considering',
        'despite', 'down', 'during', 'except', 'excepting', 'excluding',
        'following', 'from', 'in', 'inside', 'into', 'like', 'minus',
        'near', 'off', 'of', 'on', 'onto', 'opposite', 'outside', 'over',
        'past', 'per', 'plus', 'regarding', 'round', 'save', 'since', 'than',
        'through', 'to', 'toward', 'towards', 'under', 'underneath', 'unlike',
        'until', 'up', 'upon', 'versus', 'via', 'with', 'within']

    keys = {'be':['is','am','are','was','were'],
            'do':['do','does','did'],
            'have':['has','have','had'],
            'HV' :['can','could','will','would','shall','should','may','might','ought','need','must']}

    conj = ['and','but','therefore','because','whereas','eventhough',
            'nowadays','since']

    articles = ['a','an','the']

    pronouns = ['i','you','he','she','we','they']

    nounid = ['this','that','these','those','my','your','his','her','our','their']

    dustbin = ['most','very','also','always','enough','special','nowadays']

    #EMPTY LISTS#=================(create lists here)
    noun = []
    noun_index = []
    verb = []
    verb_index = []
    prep_index = []
    conj_index = []
    about = []
    about_index = []

    #PROCESSING#==================================================

    #where are those nouns?? (finding the nouns in a paragraph)
    for i in range(len(para0)):
        if para0[i] in ['of','on'] and para0[i+1].lower() not in articles+nounid:
            noun.append(para0[i-1].lower())
            noun.append(para0[i+1].lower())
        elif para0[i].lower() in articles+nounid and para0[i+1].lower() not in keys['be']+keys['do']+keys['have']+keys['HV']+dustbin:
            noun.append(para0[i+1].lower())
        elif para0[i-1][-2:-1] == "'s":
            noun.append(para0[i].lower())
        elif '.' not in para0[i-1] and para0[i][0].isupper():
            noun.append(para0[i].lower())

    #I can't find those verbs... (finding the verbs in a paragraph)
    for i in range(len(para0)):
        if para0[i].lower() not in articles+prep+conj+noun+nounid+dustbin+pronouns:
            if para0[i] == 'to' and para0[i+1] not in articles+nounid+noun:
                verb.append(para0[i+1])
            elif para0[i][-3:-1] in "ing." and para0[i] not in noun:
                verb.append(para0[i])
            elif para0[i].isalpha():
                verb.append(para0[i])
        elif para0[i].lower() in pronouns and para0[i+1] not in dustbin+articles+nounid:
            verb.append(para0[i+1])

    #refining lists (removing the unnecessary words of the paragraph)
    for i in noun+verb:
        if i in noun and i in dustbin:
            noun.remove(i)
        elif i in verb and i in dustbin:
            verb.remove(i)
        elif i[-2:-1] == 'ly':
            verb.remove(i)

    for i in range(len(para0)):
        if para0[i] in noun:
            noun_index.append(i)
        elif para0[i] in verb:
            verb_index.append(i)

    #let's sort out the things
    noun_index.sort()
    verb_index.sort()
    prep_index.sort()
    conj_index.sort()
    noun.sort()
    verb.sort()

    #BEAUTIFICATION#===================================
    while True:
        try:
            choose = input("Do you want to choose point style?(Y/N):").lower()
            if 'y' in choose:
                print("Which style would you prefer?")
                print("(1)-  (2)->  (3)•  (4)‣  (5)-- ")
                points = ['- ','-> ','• ','‣ ','-- ']
                m = int(input("Point number(MAINPOINT):"))
                n = int(input("Point number(SUBPOINT):"))
                mainpoint = points[m-1]
                subpoint = points[n-1]
            elif 'n':
                mainpoint = "->"
                subpoint = "-"
            break
        except:
            print("Enter a point style.")

    print('Chosen mainpoint:',mainpoint)
    print('Chosen subpoint:',subpoint)

    z = 0
    capson = input("Do you want to enable noun capitalization?(Y/N):").lower()
    if 'y' in capson:
        z = z+1

    #MAINSTREAM#========================================

    # this parts converts the points based on some rules to make the output readable.

    for i in d.values():
        # the following variables measures certain features so that a string can be made into a sentence.
        a = 0
        b = 0
        u = 0
        v = 0
        conj_index.clear()
        prep_index.clear()

        for j in i:
            if j.lower() in articles+dustbin and j not in ['special','most']:
                i.remove(j)
            
    ##################CHECK HERE
        for j in range(len(i)):
            if i[j].lower() in noun + pronouns:
                a = a+1
            elif i[j].lower() in verb:
                b = b+1
            elif i[j].lower() in conj and a > 0 and b > 0:
                for k in range(j,len(i)):
                    if i[k].lower() in noun + pronouns:
                        u = u+1
                    elif i[k].lower() in verb:
                        v = v+1
                    elif (k == len(i)-1) and u>0 and v>0:
                        i[j] = mainpoint
                
                    a = 0
                    b = 0
            elif ',' in i[j] and (i[j].replace(',','')).lower() in conj:
                i[j] = mainpoint
            if ',' in i[j]:
                i[j] = i[j].replace(',','')
                i[j+1] = subpoint + ' ' + i[j+1]
            
        if mainpoint not in i[0]:
            i[0] = mainpoint + ' ' + i[0]
    ##################
        a = 0
        b = 0
        c = 0
        e = 0
        for j in range(len(i)):
            if i[j] in prep and i[j].lower() != 'of':
                c = c+1
                e = j
            elif c > 0:
                if i[j] in noun+pronouns:
                    a = a+1
                elif i[j] in verb:
                    b = b+1
                if a > 0 and b > 0:
                    i[e] = subpoint + " " + i[e]
                    a = 0
                    b = 0
                    c = 0

        if z == 1:
            for j in range(len(i)):
                if i[j].lower() in noun:
                    i[j] = i[j].upper()

    #OUTPUT#=============================
    for i in d.values():
        for j in i:
            if mainpoint in j:
                print()
                print(j, end=' ')
            elif subpoint in j:
                print()
                print('\t' + j, end=' ')
            else:
                print(j, end=' ')
