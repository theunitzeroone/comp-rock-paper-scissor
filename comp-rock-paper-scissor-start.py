from threading import Thread
from network import connect, send


def send_message():
    while True:
        send(input())


def react_on_messages(timestamp, user, message):

    global me, opponent, myChoice, opponentChoice

    # listen to who joins the channel...
    if user == 'system' and 'joined channel' in message:
        player = message.split(' ')[1]
        if player != me:
            opponent = player
            print(opponent + ' has joined!\n')
            print('Let us play!\n')
            print('Choose paper, rock or scissor:')

    # If your choice is invalid
    if user == me and message not in ['paper', 'rock', 'scissor']:
        print('You must choose paper, rock or scissor!\n')

    # Remember my choice
    if user == me and message in ['paper', 'rock', 'scissor']:
        myChoice = message

    # Remember the opponent's choice
    if user == opponent and message in ['paper', 'rock', 'scissor']:
        opponentChoice = message

    # Both me and my opponent have made choices
    if myChoice != '' and opponentChoice != '':
        print('\nYou chose ' + myChoice)
        print('and ' + opponent + ' chose ' + opponentChoice)
        # now we can determine who has won (this round)
        # YOU HAVE TO WRITE THE CORRECT CODE FOR ALL
        # POSSIBILITIES INCLUDING A DRAW/TIE HERE!
#        if myChoice == 'paper' and opponentChoice == 'scissor':
#            print('You lost!')
#        elif myChoice == 'scissor' and opponentChoice == 'paper':
#            print('You won!')
        if myChoice == opponentChoice:
            print("it's a tie!")
        if myChoice == 'rock' and opponentChoice == 'scissor':
            print('You won!')
        if myChoice == 'rock' and opponentChoice == 'paper':
            print('You lost!')
        if myChoice == 'scissor' and opponentChoice == 'rock':
            print('You lost!')
        if myChoice == 'scissor' and opponentChoice == 'paper':
            print('You won!')
        if myChoice == 'paper' and opponentChoice == 'scissor':
            print('You lost!')
        if myChoice == 'paper' and opponentChoice == 'rock':
            print('You won!')
#        else:
            # and since the program is not fully written yet:
#            print('Not sure who won :(')
        # reset choices
        myChoice = ''
        opponentChoice = ''
        print('\nChoose paper, rock or scissor:')


# START -> Wait for player to enter name and channel
opponent = ''
myChoice = ''
opponentChoice = ''
me = input('Your name: ')
channel = input('Channel to join or create: ')
# connect to (or create) a channel, with a user name
connect(channel, me, react_on_messages)
# start non-blocking thread to input and send messages
Thread(target=send_message).start()
