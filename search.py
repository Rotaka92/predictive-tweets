#!/usr/bin/python
import os
import json
from twitter import Api
import urllib
import itertools
import time

config = {}
execfile("config.py", config)
# initiate python-twitter API object. http://python-twitter.readthedocs.io/
t = Api(
        config["consumer_key"],
        config["consumer_secret"],
        config["access_key"],
        config["access_secret"])
        #sleep_on_rate_limit=True)

#num = 40 # max number of people to parse through


def userSearch(term):
    term = "'" + term + "'"
    try:
        results = t.GetUsersSearch(term, page=1, count=10, include_entities=None)
        if len(results) > 0:
            return results[0].id

    except:
        print "sleeping"
        time.sleep(60*1);

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
        cells = line.split(",")
        fullName.append(cells[0].replace(' ', '') + " " + cells[2].replace(' ', ''))
        rows = rows + 1

    f.close()
    fullName.pop(0) # remove column title
    return fullName


# keywords to look for in tweets
flags = ['bomb', 'strangle', 'stab', 'decapitate', 'suicide', 'slaughter', 'assault', 'weapon', 'murder', 'rape', 'kill', 'sex', 'hate', "shoot", "revenge"];

def flagTweet(txt):
    txt = txt.lower()
    return any(sub in txt for sub in flags)


def checkTweets(user_id):
    try:
        tweetList = t.GetUserTimeline(user_id) # get latest tweets from user

        # search through user's timeline
        for tweet in tweetList:
            #print "\t" + tweet.text

            if flagTweet(tweet.text):
                print "************FLAGGED: " + str(user_id) + " (" + n + ")**************"
                print "https://twitter.com/statuses/" + str(tweet.id) + "/\n"
    except:
        print "exception" # could be due to account being set to private



users = [] # ids of found users (not guranteed to be the target's account)
print "parsing through file..."
names = readFromFile()

print "searching for " + str(len(names)) + " users...\n\n"
for n in names:
    #print " searching for account for " + n
    user_id = userSearch(n);

    if user_id != 0:
        #print "\n\n\n_______found account " + str(user_id) + " for " + n + "__________ "
        users.append(user_id)
        checkTweets(user_id)

        #print "\n\n________analyzing " + str(user_id) + " (" + n + ")________"
        time.sleep(2); # slow down output for demonstration purposes


print "\n\nscript complete"
