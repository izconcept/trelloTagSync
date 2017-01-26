# A simple adjacency matrix graph data structure
from difflib import SequenceMatcher as stringMatcher
class simpleTagGraph:
    nodes = {}
    weights = []
    tagList = []

    # Initialize the weights array and automatically generate and store the sequenceMatcher similarity as weights
    def __init__(self, tagList):
        self.weights = [[0] * len(tagList) for i in range(len(tagList))]
        self.tagList = tagList
        for x in range(0, len(tagList)):
            self.nodes[tagList[x]] = x
            for y in range(0, len(tagList)):
                if x == y:
                    self.weights[x][y] = 0
                else:
                    self.weights[x][y] = stringMatcher(None, tagList[x], tagList[y]).ratio()

    # Returns the set of weights corresponding to a node
    def getWeights(self, tagName):
        return self.weights[self.nodes[tagName]]

    def printNodes(self):
        print self.nodes

    # Prints the adjacency matrix graph
    def printGraph(self):
        row_format = "{:>18}" * (len(self.tagList) + 1)
        print row_format.format("", *self.tagList)
        for tagName, row in zip(self.tagList, self.weights):
            print row_format.format(tagName +" |", *row)