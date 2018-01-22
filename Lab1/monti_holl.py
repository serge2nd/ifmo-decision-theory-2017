import numpy

def monti_holl(saveChoice: bool,doorAmount: int,carAmout: int,openPerStep: int,nannyPerStep: int):
    doorVector = numpy.append(numpy.ones((carAmout,), dtype=numpy.int), numpy.zeros((doorAmount-carAmout,), dtype=numpy.int))
    numpy.random.shuffle(doorVector)
    choicedIndexes = [0]
    currentChoicedDoor = 0

    G = 0
    while G < nannyPerStep:
        for i in reversed(range(doorAmount)):
            if (not i in choicedIndexes and doorVector[i] == 0 ):
                choicedIndexes.append(i)
                G+=1
                break

    M = 0
    while M < (openPerStep-nannyPerStep):
        for i in reversed(range(doorAmount)):
            if (not i in choicedIndexes and doorVector[i] == 1 ):
                choicedIndexes.append(i)
                M+=1
                break

    if (not saveChoice):
        while (currentChoicedDoor in choicedIndexes):
            currentChoicedDoor+=1

    return doorVector[currentChoicedDoor] == 1

def alogoritm(saveChoice: bool,doorAmount: int,carAmout: int,openPerStep: int,nannyPerStep: int):
    # I don't know formula for this(((
    n = openPerStep-nannyPerStep
    if saveChoice:
        return carAmout/doorAmount
    else:
        return (carAmout*(carAmout - n-1)+(doorAmount-carAmout)*(carAmout-n))/(doorAmount*(doorAmount-n-nannyPerStep-1))