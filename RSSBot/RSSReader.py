import urllib.request
from urllib.error import URLError
import xml.etree.ElementTree as ET
#from time import strptime, mktime

#PUBDATEFORMAT = "%a, %d %b %Y %H:%M:%S %z"

def get_new_articles(source):
	articles = []
	try:
		response = urllib.request.urlopen(source)
		orig_rss = response.read().decode("utf-8")
		rss = ET.fromstring(orig_rss)
		channel = rss.find("channel")
		
		for item in channel.findall("item"):
			# Not used anymore
			# pubDate = item.find("pubDate").text
			# pubDateConv = mktime(time.strptime(pubDate, PUBDATEFORMAT)))
			
			link = item.find("link").text
			
			title = item.find("title")
			
			if title is not None:
				title = title.text
			if title is None:
				print("found no title, will use link")
				title = link
			
			guid = item.find("guid")
			
			if guid is not None:
				guid = guid.text
			if guid is None:
				#print("found no guid, will use link")
				guid = link
			articles.append((title, link, guid))
		
	except URLError as e:
		print("Error:", e.reason)
	
	return articles