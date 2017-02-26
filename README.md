# predictive-tweets
Project Created for [Hack UMBC Fall 2016](https://hackumbc.org/)

####PURPOSE:####
To parse through lists of criminal offenders and attempt to find their twitter accounts and flag tweets that could indicate potential threats.

####REQUIREMENTS:####
* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [Offender Data in CSV File](http://offender.fdle.state.fl.us/offender/publicDataFile.do)
* [python-twitter module](http://python-twitter.readthedocs.io/)

####RESULTS:####
The python code is able to iteratre through the csv file and search for the full name of offenders on twitter and view the latest tweets of the first user result.  These tweets are then flagged simply by whether they contain keywords stored in the array flags[ ].  

####Limitations:####
* Some people have the same names as offenders, so searching for offenders' accounts based soley on names is not always accurate.
* The Twitter API [limits](https://dev.twitter.com/rest/public/rate-limits) the amount of requests that can be made per 15 minutes.

####Future Ideas:####
Create a website that embeds the flagged tweets next to side by side pictures of the Twitter user and the offender to allow humans to easily to make their own conclusion about the tweets and act accordingly.

####CONTRIBUTORS:####
* Daniel Engbert
* Marios Levi
