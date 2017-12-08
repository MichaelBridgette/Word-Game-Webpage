with open('Words.txt', errors = 'ignore') as df:
    rawData = df.read()

import time

startTimer = False
totalTime= time.time() #start timer




allUsedWords=[]
invalidWords=[]
shortWords=[]
longWords=[]

words = rawData.split()
totalWords = len(words)

from random import randint

#get words with 7 or more letters
def GetPuzzleWordList():
    puzzleList = []
    for x in words:
        if(len(x) >= 7):
            puzzleList.append(x)
    return puzzleList

listOfPuzzles = GetPuzzleWordList()

#get the words that the player can use to guess with
def GetUsableWords(lettersAmount):
    usableWords= []
    for x in words:
        if(len(x) < lettersAmount):
            if(len(x) > 2):
                usableWords.append(x.lower())
    return usableWords

#check if a is contained within b
def intersect(a, b):
    if len(b) < len(a):  # if b is shorter than a
        a, b = b, a      # swap the lists.
    b = b[:]  # To prevent modifying the lists
    return [b.pop(b.index(i)) for i in a if i in b]

import pickle

#display the 10 highscores
def displayLeaderboard():
    place = 1
    count = 1
    for x in leaderboard:
        if(count <= 10):
            print(place,")",x, round(data[x], 2))
            place+=1
            count+=1

#add player to the highscores list
def updateLeaderboard(name , totalTime):

    with open('Players.pickle', 'rb') as pf:
        data = pickle.load(pf)             #load data from pickle file

    data[name] = totalTime #add new player
    with open('Players.pickle', 'wb') as pf:
        pickle.dump(data, pf)              #Put updated data back

    sorted(data, key=data.get)
    leaderboard = sorted(data, key=data.get)   #sort into a list

    place = 1
    count = 1
    #display top 10 players
    for x in leaderboard:

        if(count <= 10):

            print(place,")",x, round(data[x], 2))
            place+=1
            count+=1

#get the players position on the leaderboard
def getLeaderboardPosition(name):

    with open('Players.pickle', 'rb') as pf:
        players = pickle.load(pf)

    #sorted(players, key=players.get)
    leaderboard = sorted(players, key=players.get)
    counter = 0
    for i in leaderboard:
        if i == name:
            return counter+1
            print("Your Leaderboard position:", counter+1 )
        counter+=1

def getLeaderBoardList():
    with open('Players.pickle', 'rb') as pf:
        thePlayers = pickle.load(pf)

    #sorted(players, key=players.get)
    theLeaderboard = sorted(thePlayers, key=thePlayers.get)
    board =[]
    counter = 1
    for name in theLeaderboard:

        if(counter <= 10):

            board.append(name)
            counter+=1

    return board

def getPlayerDict():
    with open('Players.pickle', 'rb') as pf:
        thePlayers = pickle.load(pf)

    return thePlayers
def roundPlayerDict(board ,thePlayers):

    for name in board:
        thePlayers[name] = round(thePlayers[name],2)
    return thePlayers


def getSourceWord():
    sourceList = GetPuzzleWordList()
    source = sourceList[randint(0, len(listOfPuzzles))]
    return source

#check for input if the player wants to play again
def playAgain():
    playGame = False
    while True:
        playAgain = input("Do you want to play again?(y/n): \n")

        if playAgain == 'y':
            playGame = True
            break
        if playAgain == 'n':
            playGame = False
            break

    return playGame


def checkWords(puzzleWord , listOfAnswers):
    listOfUsableWords = GetUsableWords(len(puzzleWord)) #get a list of words that can be used
    usedWords = []
    wordCount = 0
    foundWord = False
    wordUsed = False

    print(puzzleWord)

    for answer in listOfAnswers:
        print(answer)
        if intersect(list(puzzleWord.lower()), list(answer.lower())) == list(answer.lower()) and answer.lower() in listOfUsableWords and answer.lower() != puzzleWord.lower():
            foundWord = True
        else:
            foundWord = False
            if len(answer)< 3:
                shortWords.append(answer.lower())
            elif len(answer)> len(puzzleWord):
                longWords.append(answer.lower())
            else:
                invalidWords.append(answer.lower())



#****************************************************************
        if foundWord == True:
            for x in usedWords:
                if x == answer.lower():
                    wordUsed = True
                    allUsedWords.append(answer.lower())


            if wordUsed == False:
               usedWords.append(answer.lower())
               wordCount += 1
               foundWord = False

        wordUsed = False

        if wordCount == 7:
            return True
    return False


def getInvalidWords():
    return list(set(invalidWords))

def getUsedWords():
    return list(set(allUsedWords))

def getShortWords():
    return list(set(shortWords))

def getLongWords():
    return list(set(longWords))

def clearInvalidWords():
    invalidWords[:]=[]

def clearUsedWords():
    allUsedWords[:]=[]

def clearShortWords():
    shortWords[:]=[]

def clearLongWords():
    longWords[:]=[]


def startTimer():
    global startTimer
    if startTimer is False:
        totalTime= time.time()
        startTimer = True

def stopTimer():
    global startTimer
    if startTimer is True:

        t1 = time.time()
        total = t1 - totalTime
        startTimer = False
        return total
#while True:
#    print("Welcome to my Word Game.\nYou need to get 7 words made up of a randomly generated word.\nType in a word and press Enter")
#    start  = input("Press Enter when your ready to play!")
#    break


#import time

#while True:
#    wordCount = 0
#    foundWord = False
#    wordUsed = False
#    puzzleWord = listOfPuzzles[randint(0, len(listOfPuzzles))] #get random puzzle word
#    listOfUsableWords = GetUsableWords(len(puzzleWord)) #get a list of words that can be used
#    usedWords = []

#    print('Make words out of' , puzzleWord )

#    t0 = time.time() #start timer
#    while True:

        #force player to type something
#        while True:
#            target = ""
#            target  = input("Please enter a Word: ")
#            if len(target) > 0:
#                break

        #check if the player has found a word that is acceptable
#        if intersect(list(puzzleWord.lower()), list(target.lower())) == list(target.lower()) and target.lower() in listOfUsableWords and target.lower() != puzzleWord.lower():
#            foundWord = True

#        else:
#            foundWord = False
#            print("Not a valid Word!\n")

#        if foundWord == True:
#            for x in usedWords:
#                if x == target.lower():
#                    print("Word already used!!!\n")
#                    wordUsed = True


#            if wordUsed == False:
#                usedWords.append(target.lower())
#                print("Word Found!!!")
#                wordCount += 1
#                print(7 - wordCount, "remaining\n")
#                foundWord = False

#            wordUsed = False

            #seven words mean they win
#            if wordCount == 7:
#                t1 = time.time()
#                total = t1-t0
#                name = input("What is your name? ")
#                print("YOU WIN", name.upper(), "!\n")
#                print("Time:",round(total, 2), "seconds\n\n")
#                print("\n")
#                print("LEADERBOARD")
#                print("***********")
#                updateLeaderboard(name, total)
#                print("\n")
#                getLeaderboardPosition(name)
#                print("\n")
#                break

#    if playAgain() == False:
#        break
