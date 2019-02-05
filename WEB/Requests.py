from bs4 import BeautifulSoup
import urllib.request
import json

domain = "http://127.0.0.1:8000"
urls = ["", "/site.html", "/example.html", "/site/subsite.html", "/site/other_site.html"]

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
		links["links"].append(link.get('href'))
		# print(link.get('href'))

print(json.dumps(data, indent=2, sort_keys=True))


