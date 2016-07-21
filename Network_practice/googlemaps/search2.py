#!/bin/python

import urllib,urllib2
try:
	import json
except ImportError:
	import simplejson as json

params={'q':'207 N. DEfinance St, Archbold, OH','output':'json','oe':'utf8'}

url='http://maps.google.com/maps/geo?'+urllib.urlencode(params)

rawreply=urllib2.urlopen(url).read()
print(rawreply)
reply=json.loads(rawreply)
print(reply['Placemark'][0]['Point']['Coordinate'][:-1])


