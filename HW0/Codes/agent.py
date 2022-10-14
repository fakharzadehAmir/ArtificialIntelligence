import random
import itertools
#################################################################################
# Functions
#################################################################################

def ai_action(game_state):
    ''' Generate and play move from tic tac toe AI'''
    #################################################################################
    # "*** YOUR CODE HERE ***"

    # Function for check winner's condition
    def winner_checker(gameState, placeValue):
        checker = [placeValue, placeValue, placeValue, placeValue]
        return gameState[0:4] == checker or gameState[1:5] == checker or gameState[5:9] == checker or gameState[6:10] == checker or gameState[10:14] == checker or gameState[11:15] == checker or gameState[15:19] == checker or gameState[16:20] == checker or gameState[20:24] == checker or gameState[21:25] == checker or [gameState[i] for i in [0, 5, 10, 15]] == checker or [gameState[i] for i in [5, 10, 15, 20]] == checker or [gameState[i] for i in [1, 6, 11, 16]] == checker or [gameState[i] for i in [6, 11, 16, 21]] == checker or [gameState[i] for i in [2, 7, 12, 17]] == checker or [gameState[i] for i in [7, 12, 17, 22]] == checker or [gameState[i] for i in [3, 8, 13, 18]] == checker or [gameState[i] for i in [8, 13, 18, 23]] == checker or [gameState[i] for i in [4, 9, 14, 19]] == checker or [gameState[i] for i in [9, 14, 19, 24]] == checker or [gameState[i] for i in [0, 6, 12, 18]] == checker or [gameState[i] for i in [6, 12, 18, 24]] == checker or [gameState[i] for i in [1, 7, 13, 19]] == checker or [gameState[i] for i in [5, 11, 17, 23]] == checker or [gameState[i] for i in [4, 8, 12, 16]] == checker or [gameState[i] for i in [8, 12, 16, 20]] == checker or [gameState[i] for i in [3, 7, 11, 15]] == checker or [gameState[i] for i in [9, 13, 17, 21]] == checker

    # Check game is over
    if game_state.count(2) > 0:
        return

    emptyStates = [i for i in range(0, 25) if game_state[i] is None]
    checkStates = [False, True]

    # Center
    if game_state[12] is None:
        return 12
    # 1 place to win or lose
    for turn in checkStates:
        for firstIndex in emptyStates:
            copyGame = game_state[:]
            copyGame[firstIndex] = turn
            if winner_checker(copyGame, turn):
               return firstIndex

    # 2 place to win or lose
    for turn in checkStates:
        for centralIndex in [6, 8, 16, 18]:
            for possibleIndex in emptyStates:
                copyGame = game_state[:]
                copyGame[centralIndex], copyGame[possibleIndex] = turn, turn
                if centralIndex in emptyStates and winner_checker(copyGame, turn):
                    return centralIndex
    ########################
    for turn in checkStates:
        for centralIndex in [7, 11, 13, 17]:
            for possibleIndex in emptyStates:
                copyGame = game_state[:]
                copyGame[centralIndex], copyGame[possibleIndex] = turn, turn
                if centralIndex in emptyStates and winner_checker(copyGame, turn):
                    return centralIndex
    ########################
    for turn in checkStates:
        for firstIndex, secondIndex in itertools.product(emptyStates, repeat=2):
            copyGame = game_state[:]
            copyGame[firstIndex], copyGame[secondIndex] = turn, turn
            if winner_checker(copyGame, turn):
               return firstIndex

    # 3 place to win or lose
    for turn in checkStates:
        for centralIndex in [6, 8, 16, 18]:
            for possibleIndex1, possibleIndex2 in itertools.product(emptyStates, repeat=2):
                copyGame = game_state[:]
                copyGame[centralIndex], copyGame[possibleIndex1], copyGame[possibleIndex2] = turn, turn, turn
                if centralIndex in emptyStates and winner_checker(copyGame, turn):
                    return centralIndex
    ########################
    for turn in checkStates:
        for centralIndex in [7, 11, 13, 17]:
            for possibleIndex1, possibleIndex2 in itertools.product(emptyStates, repeat=2):
                copyGame = game_state[:]
                copyGame[centralIndex], copyGame[possibleIndex1], copyGame[possibleIndex2] = turn, turn, turn
                if centralIndex in emptyStates and winner_checker(copyGame, turn):
                    return centralIndex

    ########################
    for turn in checkStates:
        for firstIndex, secondIndex, thirdIndex in itertools.product(emptyStates, repeat=3):
            copyGame = game_state[:]
            copyGame[firstIndex], copyGame[secondIndex], copyGame[thirdIndex] = turn, turn, turn
            if winner_checker(copyGame, turn):
               return firstIndex
    # Possible places for game at the end
    return random.choice(emptyStates)
    #################################################################################


    # https://s24.picofile.com/file/8453736992/Rec_0008.mp4.html