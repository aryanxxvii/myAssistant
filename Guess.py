import random
import time
import os

def pickword():
    words = ['chair', 'guitar', 'piano', 'python',  
            'floor', 'space', 'magic', 'circle',  
            'reverse', 'water', 'sunshine', 'round',
            'roomy', 'art', 'meat', 'cent', 'crime',
            'complete', 'avoid', 'scream', 'respect',
            'fascinated', 'understood', 'quirky',
            'impress', 'reduce', 'simplistic',
            'encouraging', 'day', 'toys', 'cemetery',
            'grate', 'stick', 'guess', 'needy', 'apologise',
            'boundless', 'sore', 'quartz', 'marvelous',
            'resonant', 'wail', 'puny', 'attach', 'stingy',
            'ill-informed', 'whirl', 'collect', 'screeching', 
            'physical', 'fact', 'giraffe', 'faint', 'discovery', 
            'error', 'oven', 'comparison', 'wanting', 'sweater', 
            'change', 'level', 'slave', 'tired', 'dogs', 'consider', 
            'rabbit', 'ants', 'smelly', 'gather', 'yell', 'payment', 
            'incredible', 'perfect', 'lying', 'oil', 'sturdy', 'wrap', 
            'female', 'evanescent', 'delirious', 'bite', 'range', 
            'puffy', 'tongue', 'nose', 'fat', 'needle', 'spoon', 'horrible', 
            'thrill', 'vagabond', 'ball', 'fry', 'boorish', 'two', 'jaded', 
            'rate', 'ask', 'gruesome', 'spade', 'blow', 'flippant', 'vase', 
            'suffer', 'crush', 'simple', 'comb', 'debt', 'trashy', 'arrive', 
            'penitent', 'calculator', 'trot', 'introduce', 'violet', 'frail', 
            'recess', 'dinosaurs', 'witty', 'cow', 'behavior', 'questionable', 
            'scarce', 'fail', 'disagree', 'previous', 'serve', 'hum', 'shocking', 
            'song', 'stroke', 'things', 'savory', 'invent', 'zoom', 'film', 
            'sheet', 'team', 'suggest', 'egg', 'manage', 'determined', 'doll', 
            'workable', 'gorgeous', 'knot', 'animated', 'dock', 'mature', 'delay', 
            'intend', 'reward', 'smart', 'holistic', 'snail', 'need', 'beam', 
            'crawl', 'damp', 'furniture', 'saw', 'quack', 'tent', 'unadvised', 
            'territory', 'quarrelsome', 'abortive', 'superb', 'crayon', 'true', 
            'trace', 'uttermost', 'outgoing', 'tiny', 'mundane', 'woman', 
            'quicksand', 'dress', 'neat', 'dislike', 'spicy', 'yoke', 'steadfast', 
            'coast', 'search', 'touch', 'grey', 'defiant', 'coach', 'songs', 
            'powder', 'used', 'dam', 'hospitable', 'auspicious', 'adjoining', 
            'fuel', 'hair', 'bump', 'fretful', 'legal', 'tug', 'terrible', 'annoyed', 
            'carriage', 'first', 'damaged', 'camp', 'pine', 'help', 'dark', 'post']
    

    word = random.choice(words)
    return word

def remarks():

    comments = ['Go on a wild goose chase', 'Good things come to those who wait',
    'He has bigger fish to fry', 'He is a chip off the old block']

    comment = random.choice(comments)
    return comment

def start():

    word = pickword()
    
    guesses = ''

    turns = len(word) + 5
    print("You will get", turns, "guesses.")
    
    while turns > 0:

        print("\nGood Luck ! ")
        print("Guess the characters\n")
        
        
        failed = 0
            
        for char in word:  
            
            if char in guesses:  
                print(char, end = " ") 
                
            else:  
                print("_", end = " ") 
                failed += 1
                
        if failed == 0: 
        
            print("You Win")
            print("The word is: ", word)

            return True
            break
        
        print()

        guess = input("\nGuess a character:")
        
        time.sleep(1); os.system('cls')
        
        guesses += guess  
        
        
        if guess not in word: 
            
            turns -= 1
            
            
            print("Wrong")
            
            print()
            comm = remarks()
            print(comm)
            print()
            
            print("You have", + turns, 'more guesses') 
            
            
            if turns == 0: 
                print("You Lose")
                return False
        
        else:

            print("Correct")
