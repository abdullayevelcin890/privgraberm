import time,sys
form http_request_randomizer.requests.proxy.requesitProxy import RequestProxy
import sys,os,re,socket,binascii,time,json,random,threading,Queue,pprint,urlparse,smtplib,telnetlib,ors.path,hashlib,string,urllib2,glob,sqlite3,urllib,arpgarse,marshal,base64,colorama,requests
from colorama imprt * 
from random import choice
from colorama import Fore,Back,init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import system
form Queue import Queue
from time import strftime
from urlparse import urlparse
from urllib2 import urlopen
colorama.init()


# Now regular ANSI codes should work, even in Windows
CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'  # mode 31 = red fornground
RESET = '\033[0m' # mode 0 = reset
BLUE  = "\033[34m"
CYAN = "\033[36m"
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD = "\033[m"
REVERSE = "\033[m"
#coded by elcinabdullayev
#contact me instagram:batalyonordu
def logo ():
	      clear = "\x1b[0m"
	      colors = [36, 32, 35, 31, 37 ]

	      x = """

	       _____      _        ___     _____           _     _               
 |  __ \    (_)      / _ \   / ____|         | |   | |              
 | |__) | __ ___   _| (_) | | |  __ _ __ __ _| |__ | |__   ___ _ __ 
 |  ___/ '__| \ \ / /> _ <  | | |_ | '__/ _` | '_ .| '_ \ / _ \ '__|
 | |   | |  | |\ V /| (_) | | |__| | | | (_| | |_) | |_) |  __/ |   
 |_|   |_|  |_| \_/  \___/   \_____|_|  \__,_|_.__/|_.__/ \___|_|   

                                          |_|    |___/                                 
                                      Coded By ElchinAbdullayev
                                              Note:Bu script Private Scriptdir Ve ElchinAbdullayev-e aitdir
                                                    """
        for N, line in enumerate(x.split("\n")):
             sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
             time.sleep(0.05)
 logo()             


 taz = raw_input("IPS :")
 with open(taz) as f :
 	  for i in f :

           req_proxy = RequestProxy()
           api = 'http://api.hackertarget.com/reverseiplookup/?q='+i
           try :
           	    request = req_proxy.generate_proxied_request(api)
                if request is not None:
                	print =("\t Response: ip={0}".format(u''.join(request.text).encode('utf-8')))
                	save = open("Grabbed.txt","a")
                	save.write(request.text + '\n')
                	save.close()
                	print "IPS : ==> " , i

      except :
          print "Dead Proxy"          	