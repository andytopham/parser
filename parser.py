#!/usr/bin/python
""" Testing feedparser.
	sudo pip install feedparser
"""
import feedparser
import oled
import time

myOled = oled.oled()
oldstring = ""
print "Fetching BBC headlines"

# d = feedparser.parse('http://feedparser.org/docs/examples/atom10.xml')
#d = feedparser.parse('http://www.theregister.co.uk/data_centre/cloud/headlines.atom')

d = feedparser.parse('http://feeds.bbci.co.uk/news/technology/rss.xml')
#print d['feed']['title']
print d.feed.title
#print d.entries[0].title
for i in d.entries:
#	print i.title[0:5]
	start=0
	if i.title[0:5] != "VIDEO":
#		print i.title
		if oldstring == "":
			oldstring = i.title
		else:
			while start < len(oldstring):
				padding = 16 - len(oldstring) + start
				if len(oldstring[start:]) < 12:
					myOled.writerow(1,oldstring[start:]+" ** "+i.title[0:padding])
				else:
					myOled.writerow(1,oldstring[start:]+" ** ")
				start += 1
				time.sleep(.2)
		oldstring = i.title
		

