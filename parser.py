#!/usr/bin/python
""" Testing feedparser.
	sudo pip install feedparser
"""
import feedparser
import oled
import time

def output(outputstring):
	myOled.writerow(1,outputstring[0:16])
	print outputstring[0:16]
	print start, len(oldstring[start:]), padding, divstart

myOled = oled.oled()
myOled.writerow(2,"Testing....      ")
divider = " ** "
oldstring = ""
print "Fetching BBC headlines"

#d = feedparser.parse('http://feedparser.org/docs/examples/atom10.xml')
#d = feedparser.parse('http://www.theregister.co.uk/data_centre/cloud/headlines.atom')

d = feedparser.parse('http://feeds.bbci.co.uk/news/technology/rss.xml')
print d.feed.title
for i in d.entries:
	start=0
	divstart=0
	if i.title[0:5] != "VIDEO":
		if oldstring == "":
			oldstring = i.title
		else:
			while start < (len(oldstring)+len(divider)):
				padding = 16 - len(oldstring) - len(divider) + start
				if (start > len(oldstring)):
					divstart += 1
				outputstring = oldstring[start:]+divider[divstart:]+i.title[0:padding]
				output(outputstring)
				start += 1
				time.sleep(.2)
		oldstring = i.title
		

