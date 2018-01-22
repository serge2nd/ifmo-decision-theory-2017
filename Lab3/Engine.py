import numpy


class Node:
    def __init__(self, input2dArray):
        self.input2dArray = numpy.array(input2dArray)
        self.relations = numpy.array([])
        self.nimFuncValue = None

    def getArray(self):
        return self.input2dArray

    def getSize(self):
        rows, columns = self.input2dArray.shape
        return rows

    def getHash(self):
        hash = ''
        for item in self.input2dArray.flatten():
            hash += '_' if item == numpy.inf else '1' if item == Engine.PL else '0'
        return hash

    def addRelation(self, relation):
        self.relations = numpy.append(self.relations, [relation])

    def getRelations(self):
        return self.relations

    def setValue(self, row, column, value):
        self.input2dArray[row][column] = value

    def getNimFuncValue(self):
        return self.nimFuncValue

    def setNimFuncValue(self, nimVal):
        self.nimFuncValue = nimVal

    def calcNim(self):
        summ = 0
        for relation in self.relations:
            summ += relation.getNimFuncValue()
        return summ/len(self.relations) if summ > 0 else 0


class NodeRelation:
    def __init__(self, fromRelation, toRelation, move, transformation=None, koof=1):
        self.transformation = transformation
        self.move = move
        self.koof = koof
        self.toRelation = toRelation
        self.fromRelation = fromRelation

    def getMove(self):
        return self.move

    def getTo(self):
        return self.toRelation

    def getFrom(self):
        return self.fromRelation

    def getNimFuncValue(self):
        return self.toRelation.getNimFuncValue() * self.koof


class Transformation:
    T90 = 1
    T180 = 2
    T270 = 3

    def __init__(self, type):
        self.type = type

    def transformNodeArray(self, node):
        newArray = node.getArray()
        for i in range(0, self.type):
            newArray = numpy.rot90(node.getArray())
        return newArray

    def transformMoveBack(self, move, size):
        row, column = move
        for i in range(0, self.type):
            newRow = column
            newColumn = size - row - 1
            row = newRow
            column = newColumn
        return row, column


class DefaultNodeProcessor:
    PL = 1
    PC = 0

    def __init__(self, initNode):
        """

        :type initNode: Node
        """
        self.nodeHashes = {initNode.getHash(): initNode}
        self.initNode = initNode

    def buildGraph(self, who):
        self.buildNode(self.initNode, who)

    def buildNode(self, node, who):
        """

                :type node: Node
        """
        self.nodeHashes[node.getHash()] = node
        winner = self.getWinner(node)
        if (winner != None):
            if (winner == Engine.PC):
                node.setNimFuncValue(100)
            if (winner == Engine.PL):
                node.setNimFuncValue(0)
            return node
        positions = self.findAvailableWays(node)
        if (len(positions) < 1):
            node.setNimFuncValue(50)
            return node

        for [row, column] in positions:
            newArray = numpy.copy(node.getArray())
            newNode = Node(newArray)
            newNode.setValue(row, column, who)
            existedNode, transformation = self.findExistedNodeWithTranformation(newNode)
            if (None == existedNode):
                existedNode = self.buildNode(newNode, Engine.PC if who == Engine.PL else Engine.PL)
            if transformation:
                w = None
            node.addRelation(NodeRelation(node, existedNode, [row, column], transformation))

        nim = node.calcNim()
        node.setNimFuncValue(nim)

        return node

    def findExistedNodeWithTranformation(self, node):
        existedNode = self.nodeHashes.get(node.getHash())
        if existedNode != None:
            return existedNode, None
        for type in [Transformation.T90, Transformation.T180, Transformation.T270]:
            transform = Transformation(type)
            transformedNode = Node(transform.transformNodeArray(node))
            existedNode = self.nodeHashes.get(transformedNode.getHash())
            if existedNode != None:
                return existedNode, transform
        return None, None

    def findAvailableWays(self, node):
        """

        :type node: Node
        """
        playerPositions = numpy.argwhere(node.getArray() == Engine.PL)
        pcPositions = numpy.argwhere(node.getArray() == Engine.PC)
        emptyPositions = numpy.argwhere(node.getArray() == numpy.inf)
        findedPositions = numpy.array([])
        return emptyPositions

    def getWinner(self, node):
        narray = node.getArray()
        rows, columns = narray.shape
        summDiagMain = {Engine.PC: 0, Engine.PL: 0}
        summDiagNotMain = {Engine.PC: 0, Engine.PL: 0}
        for i in range(0, rows):
            summColumn = {Engine.PC: 0, Engine.PL: 0}
            summRow = {Engine.PC: 0, Engine.PL: 0}
            for j in range(0, columns):
                if (narray[i][j] in [Engine.PC, Engine.PL]):
                    summRow[narray[i][j]] += 1
                if (narray[j][i] in [Engine.PC, Engine.PL]):
                    summColumn[narray[j][i]] += 1
                    # diagonals
                if (i == j and narray[i][j] in [Engine.PC, Engine.PL]):
                    summDiagMain[narray[i][j]] += 1
                if i == (columns - 1 - j) and narray[i][j] in [Engine.PC, Engine.PL]:
                    summDiagNotMain[narray[i][j]] += 1
            for summ in [summColumn, summRow]:
                if (summ[Engine.PL] >= rows):
                    return Engine.PL
                if (summ[Engine.PC] >= rows):
                    return Engine.PC
        for summ in [summDiagMain, summDiagNotMain]:
            if (summ[Engine.PL] >= rows):
                return Engine.PL
            if (summ[Engine.PC] >= rows):
                return Engine.PC
        return None

    def getBestMove(self, node):
        existedNode, transformation = self.findExistedNodeWithTranformation(node)
        bestRelation = None
        bestNimVal = 0
        if existedNode == None:
            return None

        relations = existedNode.getRelations()
        for relation in relations:
            if (relation.getNimFuncValue() > bestNimVal):
                bestNimVal = relation.getNimFuncValue()
                bestRelation = relation
        if bestRelation:
            if None != transformation:
                return transformation.transformMoveBack(bestRelation.getMove(), existedNode.getSize())
            return bestRelation.getMove()
        return None


class Engine:
    STRATEGY_DEFAULT = 'STRATEGY_DEFAULT'
    STRATEGY_EXTRA = 'STRATEGY_EXTRA'
    PL = 1
    PC = 0

    def __init__(self, strategy, size, whoFirst):
        self.strategy = strategy
        self.size = size
        self.currentNode = Node(numpy.full((size, size), numpy.inf))
        self.nodeProcessor = DefaultNodeProcessor(self.currentNode)
        self.nodeProcessor.buildGraph(whoFirst)

    def changePlayerState(self, row, column):
        self.currentNode.setValue(row, column, DefaultNodeProcessor.PL)

    def changeComputerState(self, row, column):
        self.currentNode.setValue(row, column, DefaultNodeProcessor.PC)

    def getBestMove(self):
        return self.nodeProcessor.getBestMove(self.currentNode)
