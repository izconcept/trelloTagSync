import urllib, json, graph

tagList = []
idList = []

# Get list of board IDs
response = urllib.urlopen("https://api.trello.com/1/members/5882880821001df768e97ab1/boards?fields=id&key=802bfaebca5c1949a376ae0fa56eec6e&token=4d0d125517f9dccfd1838b32ebb1fa732b196bfcf9bdd26a66a2e3c3bac1c921")
boardList = json.loads(response.read())

# Get list of labels/tags in each board and store them in tagList
for board in boardList:
    response = urllib.urlopen("https://api.trello.com/1/boards/"+board["id"]+"/cards?fields=labels&key=802bfaebca5c1949a376ae0fa56eec6e&token=4d0d125517f9dccfd1838b32ebb1fa732b196bfcf9bdd26a66a2e3c3bac1c921")
    labelList = json.loads(response.read())
    for labels in labelList:
        for label in labels['labels']:
            if label["id"] not in idList and label.has_key("name"):
                tagList.append(label["name"])
                idList.append(label["id"])

# Declaring my graph data structure and storing my tags inside it
tagGraph = graph.simpleTagGraph(tagList)

# Printing the adjacency matrix
tagGraph.printGraph()

#Printing Clusters
print tagGraph.cluster()