import random

def getFiveRandom(answer, colorOptions: list) -> list:
    numOptions = len(colorOptions)
    correctIx = random.randrange(0, 5, 1)    
    outputList = []
    while len(outputList) < 4:
        # Get a potential color
        colorIx = random.randrange(0, numOptions)
        color = colorOptions[colorIx]
        if (color != answer):
            outputList.append(color)
    
    outputList.insert(correctIx, answer)
    return outputList

def getThree(answer, colorOptions: list, correctIx: int) -> list:        
    if correctIx == 0:
        return getThreeLeft(answer, colorOptions)
    elif correctIx == 1:
        return getThreeCenter(answer, colorOptions)
    elif correctIx == 2:  
        return getThreeRight(answer, colorOptions)
    
    return None


def getThreeLeft(answer, colorOptions: list) -> list:
    answerIx = colorOptions.index(answer)
    endEntry = len(colorOptions)

    if answerIx + 2 >= endEntry:
        return None
    else:
        return [
            answer,
            colorOptions[answerIx + 1],
            colorOptions[answerIx + 2],
        ]

def getThreeCenter(answer, colorOptions: list) -> list:
    answerIx = colorOptions.index(answer)
    endEntry = len(colorOptions)

    if answerIx + 1 >= endEntry or answerIx - 1 < 0:
        return None
    else:
        return [
            colorOptions[answerIx - 1],
            answer,
            colorOptions[answerIx + 1],
        ]

def getThreeRight(answer, colorOptions: list) -> list:
    answerIx = colorOptions.index(answer) 

    if answerIx -2 < 0:
        return None
    else:
        return [
            colorOptions[answerIx - 2],
            colorOptions[answerIx - 1],
            answer,
        ]



