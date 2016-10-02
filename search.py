#!/usr/bin/python
import twitter
import json
#from twitter import *
import oauth2 as oauth
#from oauth2 import *

import requests
from requests import Session

config = {}
execfile("config.py", config)

#session = Session()

consumer = oauth.Consumer(key=config["consumer_key"], secret=config["consumer_secret"])
#o = OAuth(config["access_key"], config["access_secret"], config["consumer_key"],config["consumer_secret"])

t = twitter.Api(auth=o)



print "hello"
