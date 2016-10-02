#!/usr/bin/python
import os
import json
from twitter import Api
#import oauth2 as oauth
#from oauth2 import *

import requests
from requests import Session

config = {}
execfile("config.py", config)

#session = Session()

t = Api(config["consumer_key"], config["consumer_secret"], config["access_key"], config["access_secret"])


print "hello"
