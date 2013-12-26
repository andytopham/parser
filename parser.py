#!/usr/bin/python
""" parser.py
	This grabs a rss feed and scrolls the titles from this acros the oled display.
	Choose rss feed from command line options.
	Used as a test for feedparser and argparse.
	sudo pip install feedparser
"""
import feedparser
import oled
import time
import argparse

delay=.2
divider = " ** "

def output(outputstring):
	myOled.writerow(1,outputstring[0:16])

def defaultlink():
	d = feedparser.parse('http://feeds.bbci.co.uk/news/technology/rss.xml')
	return(d)

def newlink():
	d = feedparser.parse('http://www.theregister.co.uk/data_centre/cloud/headlines.atom')
	return(d)

def filtering(d):
	z = []
	j = 0
	for k in d.entries:
		if k.title[0:5] != "VIDEO":
			z.append(k)			# pop does not take it off the list, but returns it
			j += 1
	print "*** Number of entries: ",len(d.entries),
	print "Number of entries after remove: ",len(z)
	return(z)
		
def parsing():
	parser = argparse.ArgumentParser(description='parser.py - display the contents of a rss feed on an oled')
	parser.add_argument('-l', '--link', dest='link', action='store_true',
					   help='process this link')
	args = parser.parse_args()
	if args.link == True:
		d = newlink()
	else:
		d = defaultlink()
	print d.feed.title
	return(d,d.feed.title)
	
def showentries(filteredlist,feedtitle):
	oldstring = ""
	for j,i in enumerate(filteredlist):
		myOled.writerow(2,feedtitle[:13]+":"+str(j))
		start=0
		divstart=0
		print i.title
		if oldstring == "":
			oldstring = i.title
			continue
		while start < (len(oldstring)+len(divider)):
			padding = 16 - len(oldstring) - len(divider) + start
			if (start > len(oldstring)):
				divstart += 1
			outputstring = oldstring[start:]+divider[divstart:]+i.title[0:padding]
			output(outputstring)
			start += 1
			time.sleep(delay)
			oldstring = i.title
	# now need to just output the very last item
	start = 0
	myOled.writerow(2,"BBC Tech News:"+str(j+1))
	while start < (len(i.title)+1):
		outputstring = i.title[start:]+" "		#remember to clear the trailing char
		output(outputstring)
		start += 1
		time.sleep(delay)
	return(0)


myOled = oled.oled()
myOled.writerow(2,"Testing....      ")

d,feedtitle = parsing()
filteredlist = filtering(d)
showentries(filteredlist,feedtitle)

