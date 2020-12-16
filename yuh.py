###############################################
# Magic 8 Ball
###############################################

import random

def magicEightBall():
    # https://en.wikipedia.org/wiki/Magic_8-Ball#Possible_answers
    option = random.randint(0, 18)
    if (option == 0): return "It is certain."
    elif (option == 1): return "It is decidedly so."
    elif (option == 2): return "Without a doubt."
    elif (option == 3): return "Yes - definitely."
    elif (option == 4): return "You may rely on it."
    elif (option == 5): return "As I see it, yes."
    elif (option == 6): return "Most likely."
    elif (option == 7): return "Outlook good."
    elif (option == 8): return "Signs point to yes."
    elif (option == 9): return "Reply hazy, try again"
    elif (option == 10): return "Ask again later."
    elif (option == 11): return "Better not tell you now."
    elif (option == 12): return "Cannot predict now."
    elif (option == 13): return "Concentrate and ask again."
    elif (option == 14): return "Don't count on it."
    elif (option == 15): return "My reply is no."
    elif (option == 16): return "My sources say no"
    elif (option == 17): return "Outlook not so good."
    else: return "Very doubtful."

def playMagicEightBall():
    print('-----------------')
    print('Magic Eight Ball!')
    print('-----------------')
    input('Enter a yes/no question: ')
    response = magicEightBall()
    print('-----------------')
    print(response)
    print('-----------------')

playMagicEightBall()






