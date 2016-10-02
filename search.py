#!/usr/bin/python
import os
import json
from twitter import Api

config = {}
execfile("config.py", config)


t = Api(config["consumer_key"], config["consumer_secret"], config["access_key"], config["access_secret"])

results = t.GetSearch(
            raw_query="q=engbert%20&result_type=recent&since=2014-07-19&count=10")


results = t.GetUsersSearch("dan engbert", page=1, count=20, include_entities=None)
for i in results:
    print i
    print ""
    print ""

