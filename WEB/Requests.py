from bs4 import BeautifulSoup
import urllib.request
import json

domain = "http://127.0.0.1:8000"

urls = ["", "/site.html", "/example.html", "/site/subsite.html", "/site/other_site.html"] # available links

for x in range(0, len(urls)):
	url = domain + urls[x]
	urls[x] = url

data = {}
for url in urls:

	title = {}
	links = {}
	links["links"] = []
	title["title"] = []
	data[url] = title, links

	page = urllib.request.urlopen(url)
	html = BeautifulSoup(page.read(), "html.parser")
	title["title"] = html.title.string
	# print(html.title.string)

	for link in html.findAll('a'):
		extract = link.get('href')
		# print(link.get('href'))

		if "http://0.0.0.0:8000" in extract: # changed to local address 127.0.0.1
			extract = extract.replace("http://0.0.0.0:8000", domain)
			links["links"].append(extract)

		elif "http" not in extract:
			extract = domain + extract
			links["links"].append(extract)

		# if you want to display links from other website
		# else:
		# 	links["links"].append(x)

print(json.dumps(data, indent=2, sort_keys=True))


