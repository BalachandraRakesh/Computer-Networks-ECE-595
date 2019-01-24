import socket
import sys
import os
import datetime, time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Create a TCP/IP socket
server_ip = ["www.google.com", "www.purdue.edu", "www.twitter.com", "www.cnn.com", "www.yahoo.com", "www.facebook.com",
			 "www.instagram.com", "www.fbi.gov", "www.amazon.com", "www.snapchat.com", "www.whatsapp.com", "www.gmail.com",
			 "www.umich.edu", "www.ucsd.edu", "www.utoronto.ca", "www.youtube.com", "www.wikipedia.org", "www.reddit.com",
			 "www.netflix.com", "www.linkedin.com", "www.twitch.tv", "www.microsoft.com", "www.enjin.com", "www.quora.com", 
			 "www.salesforce.com", "www.dropbox.com", "www.xvideos.com", "www.walmart.com", "www.ebay.com", "www.wipro.com",
			 "www.apple.com", "www.paypal.com", "www.nytimes.com", "www.bing.com", "www.chase.com", "www.imdb.com", 
			 "www.intuit.com", "www.metropcs.mobi", "www.taobao.com", "www.web.mit.edu", "www.caltech.edu", "www.stanford.edu", 
			 "www.princeton.edu", "www.berkeley.edu", "www.ucla.edu", "www.harvard.edu", "www.yale.edu", "www.att.com", 
			 "www.qualcomm.com", "www.intel.com", "www.nvidia.com", "www.ti.com", "www.baxter.com", "www.northropgrumman.com", 
			 "www.hulu.com", "www.banayantree.com", "www.eurosport.com"]
for i in range(len(server_ip)):
	if not os.path.exists(server_ip[i]):
		os.makedirs(server_ip[i])
	Traceroute = os.system("date /T" + ">>" + server_ip[i] +"/" "traceroute.txt" )
	Traceroute = os.system("time /T" + ">>" + server_ip[i] +"/" "traceroute.txt" )
	Ping = os.system("date /T" + ">>" + server_ip[i] +"/" "ping.txt")
	Ping = os.system("time /T" + ">>" + server_ip[i] +"/" "ping.txt")
	Traceroute = os.system("tracert " + server_ip[i] + ">>" + server_ip[i] +"/" "traceroute.txt" )
	Ping = os.system("ping " + server_ip[i] + ">>" + server_ip[i] +"/" "ping.txt")


    

