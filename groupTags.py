#!/usr/bin/env python

import sys, json, cluster, cgi

#Retrieve POST data and convert JSON to dictionary
form = cgi.FieldStorage()

tagList = {}
for key in form.keys():
    tagList[key] = form.getvalue(key)

newCluster = cluster.simpleStringCLuster(tagList)

tagCluster = newCluster.cluster


print "Status: 200 OK"
print "Content-Type: application/json"
print ""
print json.dumps(tagCluster)

