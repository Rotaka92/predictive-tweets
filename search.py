#!/usr/bin/python
import os
import json
from twitter import Api

import urllib
import itertools

config = {}
execfile("config.py", config)
t = Api(config["consumer_key"], config["consumer_secret"], config["access_key"], config["access_secret"])

num = 40 # max number of people to parse through


def userSearch(term):
    term = "'" + term + "'"
    results = t.GetUsersSearch(term, page=1, count=20, include_entities=None)

    if len(results) < 5 and len(results) > 0:
        return results[0].id

    return 0


def readFromFile():
    img = []
    firstName = []
    lastName = []
    fullName = []
    weight = []
    rows = 0

    f = open('FLORIDA.csv', 'rU' ) # open the file in read universal mode
    for line in f:
	    if rows == num+1:
                break
	    cells = line.split(",")
	    fullName.append(cells[0].replace(' ', '') + " " + cells[2].replace(' ', ''))

	    img.append(cells[13].replace(' ', '')) # since we want only 14th column
	    firstName.append(cells[0].replace(' ', ''))
	    lastName.append(cells[2].replace(' ', ''))
	    weight.append(cells[8].replace(' ', ''))
	    rows = rows + 1

    f.close()
    img.pop(0) # remove column title
    firstName.pop(0) # remove column title
    lastName.pop(0)
    fullName.pop(0) # remove column title
    weight.pop(0)

    return fullName

    firstName = map(str.lower, firstName) # makes the names uppercase
    lastName = map(str.lower, lastName) # makes the names uppercase

    for x in range(rows-1):
	    print firstName[x] + " " + lastName[x]


names = readFromFile()
for n in names:
    res = userSearch(n);
    if res != 0:
       print res
       print ""
       print ""


    #print n + ", " + str(len(res))
print "end"
