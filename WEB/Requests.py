import urllib.request
import re
import time

domain = "http://127.0.0.1:8000"
urls = ["", "/site.html", "/example.html", "/site/subsite.html", "/site/other_site.html"]

for x in range(0, len(urls)):
	url = domain + urls[x]
	urls[x] = url

pattern = b'<title>(.+?)</title>'
result = re.compile(pattern)

for url in urls:
	htmlsource = urllib.request.urlopen(url)
	htmltext = htmlsource.read()
	titles = re.findall(result, htmltext)
	print(titles)

# with urllib.request.urlopen(url) as response:
# 	encoding = response.info().get_param('charset', 'utf8')
# 	html = response.read().decode(encoding)
# 	print(html)