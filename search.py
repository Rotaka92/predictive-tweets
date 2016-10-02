#!/usr/bin/python
import os
import json
from twitter import Api
import urllib
import itertools

config = {}
execfile("config.py", config)
# initiate python-twitter API object. http://python-twitter.readthedocs.io/
t = Api(
        config["consumer_key"],
        config["consumer_secret"],
        config["access_key"],
        config["access_secret"],
        sleep_on_rate_limit=True)

#num = 40 # max number of people to parse through


def userSearch(term):
    term = "'" + term + "'"
    results = t.GetUsersSearch(term, page=1, count=7, include_entities=None)

    if len(results) < 4 and len(results) > 0:
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
	    #if rows == num+1:
            #    break
	    cells = line.split(",")
	    fullName.append(cells[0].replace(' ', '') + " " + cells[2].replace(' ', ''))

	    #img.append(cells[13].replace(' ', '')) # since we want only 14th column
	    #firstName.append(cells[0].replace(' ', ''))
	    #lastName.append(cells[2].replace(' ', ''))
	    #weight.append(cells[8].replace(' ', ''))
	    rows = rows + 1

    f.close()
    fullName.pop(0) # remove column title
    #img.pop(0) # remove column title
    #firstName.pop(0) # remove column title
    #lastName.pop(0)
    #weight.pop(0)
    #firstName = map(str.lower, firstName) # makes the names uppercase
    #lastName = map(str.lower, lastName) # makes the names uppercase

    return fullName



# keywords to look for in tweets
flags = ['bomb', 'murder', 'rape', 'kill', 'sex', 'hate', "fuck", "vagina", "penis", "shoot", "revenge"];

def flagTweet(txt):
    txt = txt.lower()
    return any(sub in txt for sub in flags)



users = [] # ids of found users (not guranteed to be the target's account)

print "parsing through file..."
names = readFromFile()

print "searching for users...\n\n"
for n in names:
    user_id = userSearch(n);

    if user_id != 0:
        users.append(user_id)
        #print "\n\n________analyzing " + str(user_id) + " (" + n + ")________"
        tweetList = t.GetUserTimeline(user_id) # get latest tweets of user

        # search through user's timeline
        for tweet in tweetList:
            if flagTweet(tweet.text):
                #print "\n\n************FLAGGED: " + str(user_id) + "**************"
                print "https://twitter.com/statuses/" + str(tweet.id) + "/"


print "\n\nscript complete"
