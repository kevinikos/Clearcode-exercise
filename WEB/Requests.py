import urllib.request
import re
import requests
from bs4 import BeautifulSoup

domain = "http://127.0.0.1:8000"
urls = ["", "/site.html", "/example.html", "/site/subsite.html", "/site/other_site.html"]

for x in range(0, len(urls)):
	url = domain + urls[x]
	urls[x] = url

pattern = b'<title>(.+?)</title>'
result = re.compile(pattern)

data = {}
titles = {}
links = {}

for url in urls:
	data[url] = titles, links
	titles["title"] = []
	links["link"] = []

	# titles:
	htmlsource = urllib.request.urlopen(url)
	htmltext = htmlsource.read()
	title = re.findall(result, htmltext)
	titles["title"].append(title)
	print("TITLE:", title)
	# links:
	html_page = requests.get(url).text
	soup = BeautifulSoup(html_page, "lxml")
	for link in soup.findAll('a'):
		print(link.get('href'))
		links["link"].append(link.get('href'))

print(data)
# for url in urls:
# 	html_page = requests.get(url).text
# 	soup = BeautifulSoup(html_page, "lxml")
# 	for link in soup.findAll('a'):
# 		print(link.get('href'))

