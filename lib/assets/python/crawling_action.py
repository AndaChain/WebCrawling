import sys
import requests
import re
from bs4 import BeautifulSoup, SoupStrainer
def link_format(str_input):
	# if it's empty string str_out set to empty string it's mean it's not link
	domain = str_input.split(".")[1]
	if(str_input == ""):
		str_out = ""
	else:
		str_out = re.search(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))", str_input)

		# if str_out is None go to forming link to correct full link
		if(str_out == None):
			if( str_input[0:2] == "//" and len(str_input) > 3 ):
				str_out = "https:"+str_input
			elif(str_input[0] == "/" and len(str_input) > 3):
				str_out = "https://"+domain+str_input
			elif(str_input[0:2] == "./" and len(str_input) > 3):
				str_out = "https://"+domain+"/"+str_input[2:]
				#print(str_out)
			else:
				str_out = ""
		else:
			# if str_out isn't None it's mean str_out is a link can be search
			str_out = str_out.group()
			# but some values of str_out isn't exist https:// or http://
			if("https://" in str_out or "http://" in str_out):
				pass
			else:
				str_out = "https://"+str_out
            
	return str(str_out)
	
	
	
try:
	#sys.argv[1]
	url_from_ruby = link_format(sys.argv[1])
	session = requests.Session()
	#print("starting...")
	resp = session.get(url_from_ruby)
	#print("get html complete...")
	html_code = resp.content
	soup = BeautifulSoup(html_code, 'html.parser')

	descript = soup.find_all('meta',attrs={'name':'description'}) # find description tags
	for i in descript:
		print(i["content"],end="")
	print("|"+url_from_ruby)
	
except requests.exceptions.MissingSchema:
	print("error")
