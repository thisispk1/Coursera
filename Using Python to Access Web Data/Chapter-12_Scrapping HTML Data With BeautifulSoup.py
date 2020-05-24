import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
if len(url)<1:
    url = 'http://py4e-data.dr-chuck.net/comments_521896.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
num = []
count = 0
for tags in soup.find_all('span', class_='comments'):
    num.append(int(tags.text))
    count = count+1
print('Count',count)
print('Sum',sum(num))
