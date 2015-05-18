from sys import argv

user_name = ""
prompt = "> "

def killPlayer():
    print "%s has died." % user_name

def calculateUserAction(action):
    if action == "1":
        killPlayer()
    elif action == "2":
        killPlayer()
    else:
        killPlayer()
        
def greeting():
        print "Willkommen!"
        print "Let's play a game"
        print "What's your name?"
        global user_name
        user_name = raw_input(prompt)
        print "Hallo, %s!" % user_name
        startGame(False)
        
def startGame(isReplay):
    print "\n"
    
    firstObstacle = "%s, You are in an empty room with one door." % user_name
    
    if isReplay == True:
        firstObstacle += "..again."
    
    print firstObstacle
    print "1. Go through the door"
    print "2. Stay in the room"
    action = raw_input(prompt)
    calculateUserAction(action)

    print "\n"
    print "Want to play again?"
    print "1. Play Again"
    print "2. Quit playing because you're a Quitter McQuitterson"
    replay = raw_input(prompt)
    playAgain(replay)
    


def playAgain(replay):
    if replay == "1":
        startGame(True)
    else:
        print "\n"
        print "Quitter."
        exit(0)

greeting()