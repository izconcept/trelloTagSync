import json, urllib
from difflib import SequenceMatcher as stringMatcher
import requests

class simpleStringCLuster:
    cluster = []
    def __init__(self, tagList):
        poppedTags = []
        for tagId, tagName in tagList.items():
            if tagId not in poppedTags:
                subCluster = {}
                subCluster[tagId] = tagName
                poppedTags.append(tagId)
                for tagId2, tagName2 in tagList.items():
                    if stringMatcher(None, tagName.lower(), tagName2.lower()).ratio() > 0.49 and tagId2 not in poppedTags:
                        subCluster[tagId2] = tagName2
                        poppedTags.append(tagId2)
                self.cluster.append(subCluster)


    def groupTags(self, tagIDToGroupBy, cluster):
        cluster.pop(tagIDToGroupBy, None)
        idList = cluster.keys()
        boardRequest = urllib.urlopen("https://api.trello.com/1/members/5882880821001df768e97ab1/boards?fields=id&key=802bfaebca5c1949a376ae0fa56eec6e&token=4d0d125517f9dccfd1838b32ebb1fa732b196bfcf9bdd26a66a2e3c3bac1c921")
        boardList = json.loads(boardRequest.read())
        for board in boardList:
            cardResponse = urllib.urlopen("https://api.trello.com/1/boards/" + board["id"] + "/cards?fields=labels&key=802bfaebca5c1949a376ae0fa56eec6e&token=4d0d125517f9dccfd1838b32ebb1fa732b196bfcf9bdd26a66a2e3c3bac1c921")
            cardList = json.loads(cardResponse.read())
            for card in cardList:
                for label in card['labels']:
                    if label["id"] in idList:
                        r = requests.post("https://api.trello.com/1/cards/"+ card["id"] + "/idLabels/" + tagIDToGroupBy + "&key=802bfaebca5c1949a376ae0fa56eec6e&token=4d0d125517f9dccfd1838b32ebb1fa732b196bfcf9bdd26a66a2e3c3bac1c921")
                        print r.text
                        r2 = requests.delete("https://api.trello.com/1/cards/"+ card["id"] + "/idLabels/" + label["id"] + "&key=802bfaebca5c1949a376ae0fa56eec6e&token=4d0d125517f9dccfd1838b32ebb1fa732b196bfcf9bdd26a66a2e3c3bac1c921")
                        print r2.text




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