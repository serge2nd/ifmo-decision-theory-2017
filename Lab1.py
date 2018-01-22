import matplotlib.pyplot as plt
import numpy
from Lab1 import monti_holl

ITERATE_COUNT = 99


def calc(params):
    summ = 0
    summChange = 0
    for i in range(0, ITERATE_COUNT):
        summ += monti_holl.monti_holl(True, *params)
    koof = summ / ITERATE_COUNT
    for i in range(0, ITERATE_COUNT):
        summChange += monti_holl.monti_holl(False, *params)
    koofChange = summChange / ITERATE_COUNT
    algoKoof = monti_holl.alogoritm(True, *params)
    algoKoofChange = monti_holl.alogoritm(False, *params)
    return [koof, koofChange, algoKoof, algoKoofChange]


PARAMS = [
    [
        #doors,cars,openPerStep,openNanniesInStep
        [3, 1, 1, 1],
        [4, 1, 1, 1],
        [5, 1, 1, 1],
        [6, 1, 1, 1],
        [7, 1, 1, 1],
        [8, 1, 1, 1],
        [9, 1, 1, 1],
        [10, 1, 1, 1],
        [11, 1, 1, 1],
        [12, 1, 1, 1],
        [13, 1, 1, 1],
        [14, 1, 1, 1],
        [15, 1, 1, 1],
    ],
    [
        [10, 1, 1, 1],
        [10, 2, 1, 1],
        [10, 3, 1, 1],
        [10, 4, 1, 1],
        [10, 5, 1, 1],
        [10, 6, 1, 1],
        [10, 7, 1, 1],
        [10, 8, 1, 1],
    ],
    # [
    #     [40, 10, 2, 1],
    #     [40, 10, 3, 1],
    #     [40, 10, 4, 1],
    #     [40, 10, 5, 1],
    #     [40, 10, 6, 1],
    #     [40, 10, 7, 1],
    #     [40, 10, 8, 1],
    #     [40, 10, 9, 1],
    #     [40, 10, 10, 1],
    # ],
    # [
    #     [40, 10, 10, 1],
    #     [40, 10, 10, 2],
    #     [40, 10, 10, 3],
    #     [40, 10, 10, 4],
    #     [40, 10, 10, 5],
    #     [40, 10, 10, 6],
    #     [40, 10, 10, 7],
    #     [40, 10, 10, 8],
    #     [40, 10, 10, 9],
    #     [40, 10, 10, 10],
    # ]
]

graphsData = []
graphsDataChanged = []
indexFigure = 0
index = 0
for data in numpy.array(PARAMS):
    koofArray = arr = numpy.empty((0, 4))
    for params in data:
        koofArray = numpy.append(koofArray, [numpy.array(calc(params))], axis=0)
    axis = numpy.array(data)[:, index]
    # axis = range(len(data))
    plt.figure(indexFigure)
    indexFigure += 1
    #red by statictic ,second by formul
    plt.plot(axis, koofArray[:, 0], 'r--', axis, koofArray[:, 2], 'b--')

    plt.figure(indexFigure)
    indexFigure += 1
    plt.plot(axis, koofArray[:, 1], 'r--', axis, koofArray[:, 3], 'g--')
    plt.show()
    index+=1
