from difflib import SequenceMatcher as stringMatcher
class simpleTagGraph:
    nodes = {}
    weights = []

    def __init__(self, tagList):
        self.weights = [[0] * len(tagList) for i in range(len(tagList))]
        for x in range(0, len(tagList)):
            self.nodes[tagList[x]] = x
            for y in range(0, len(tagList)):
                if x == y:
                    self.weights[x][y] = 0
                else:
                    self.weights[x][y] = stringMatcher(None, tagList[x], tagList[y]).ratio()

    def getWeights(self, tagName):
        return self.weights[self.nodes[tagName]]

    def printGraph(self):
        for row in self.weights:
            for item in row:
                print "| %.3f" %(item),
            print