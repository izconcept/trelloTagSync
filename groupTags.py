#!/usr/bin/env python

import json, cgi
from difflib import SequenceMatcher as stringMatcher

# Given a list of tags, group the tags into distinct clusters
def createClusters(tagList):
    cluster = []
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
            cluster.append(subCluster)
    return cluster;

# Retrieve POST data and convert JSON to dictionary
form = cgi.FieldStorage()

# Converting fieldStorage to dicitonary
tagList = {}
for key in form.keys():
    tagList[key] = form.getvalue(key)

# Create Clusters from tagList
tagCluster = createClusters(tagList)

# Returning clustered tags
print "Status: 200 OK"
print "Content-Type: application/json"
print ""
print json.dumps(tagCluster)