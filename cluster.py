from difflib import SequenceMatcher as stringMatcher
class simpleStringCLuster:
    cluster = []
    def __init__(self, tagList):
        i = 0
        while i < len(tagList):
            subCluster = []
            currentItem = tagList.pop(i)
            subCluster.append(currentItem)
            n = 0
            while n < len(tagList):
                if stringMatcher(None, currentItem.lower(), tagList[n].lower()).ratio() > 0.49:
                    subCluster.append(tagList.pop(n))
                else:
                    n += 1
            self.cluster.append(subCluster)

    # Clusters tags into distinct group by recursively searching through the graph
    def clusterR(self, tagList, node):
        if len(tagList) == 0:
            return
        else:
            returnCluster = []
            for i in range(len(tagList)):
                if stringMatcher(None, node, tagList[i]).ratio() > 0.5:
                    returnCluster.extend(tagList.pop(i))
            for item in returnCluster:
                returnCluster.extend(self.cluster(tagList, item))
            return returnCluster