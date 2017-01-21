import urllib, json
import graph
from difflib import SequenceMatcher as stringMatcher
# HTTP call to list1

url = "https://api.trello.com/1/lists/588288bcca786b868bf78a9c/cards?key=802bfaebca5c1949a376ae0fa56eec6e&token=4d0d125517f9dccfd1838b32ebb1fa732b196bfcf9bdd26a66a2e3c3bac1c921"
response = urllib.urlopen(url)
list1 = json.loads(response.read())

url = "https://api.trello.com/1/lists/588289e01f0045d1075ff7e0/cards?key=802bfaebca5c1949a376ae0fa56eec6e&token=4d0d125517f9dccfd1838b32ebb1fa732b196bfcf9bdd26a66a2e3c3bac1c921"
response2 = urllib.urlopen(url)
list2 = json.loads(response2.read())

# Iterating through both lists and storing labels in LOWERCASE in an array/list
tagList = []
idList = []
for listItem in list1:
    for label in listItem["labels"]:
        if label["id"] not in idList:
            tagList.append(label["name"].lower())
            idList.append(label["id"])

for listItem in list2:
    for label in listItem["labels"]:
        if label["id"] not in idList:
            tagList.append(label["name"].lower())
            idList.append(label["id"])

tagGraph = graph.simpleTagGraph(tagList)
tagGraph.printGraph()