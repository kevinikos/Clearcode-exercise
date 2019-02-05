from bs4 import BeautifulSoup
import urllib.request
import json

domain = "http://127.0.0.1:8000" # input
urls = ["http://127.0.0.1:8000"] # available links
data = {}
i = 0

while 5 > urls.count(urls[-1]): # break if last argument in url list is looping

	title = {}
	links = {}
	title["title"] = []
	links["links"] = []
	last = urls[0+i] # checking each argument
	data[last] = title, links

	page = urllib.request.urlopen(last)
	html = BeautifulSoup(page.read(), "html.parser")
	title["title"] = html.title.string
	# print(html.title.string)

	for link in html.findAll('a'):
		extract = link.get('href')

		if "http://0.0.0.0:8000" in extract: # changed to local address 127.0.0.1
			extract = extract.replace("http://0.0.0.0:8000", domain)
			links["links"].append(extract)
			urls.append(extract)

		elif "http" not in extract: # added domain to half links like "/site.html"
			extract = domain + extract
			links["links"].append(extract)
			urls.append(extract)

		# if you want to display links from other website
		# else:
		# 	links["links"].append(extract)

	i += 1

print(json.dumps(data, indent=2, sort_keys=True))


