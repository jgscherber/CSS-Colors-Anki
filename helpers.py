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





