#!/usr/bin/env python
import json
import urllib2
data = json.load(urllib2.urlopen("https://github.com/mozilla-b2g/gaia/graphs/contributors-data"))
for i in xrange(100):
    if data[i]['author']['login'] == 'RickyChien':
        print 'RickyChien is currently ranked %dth among all the Gaia contributors in the world' % (100-i)
        