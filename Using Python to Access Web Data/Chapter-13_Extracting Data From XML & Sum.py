import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import ssl
import requests

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
if len(url)<1:
    url = 'http://py4e-data.dr-chuck.net/comments_521898.xml'

# html = urllib.request.urlopen(url, context=ctx).read()
html = requests.get(url).text
tree = ET.fromstring(html)
sum = 0
count = 0
for num in tree.findall('.//count'):
    # print(num.text)
    sum = sum + int(num.text)
    count = count + 1
print('Retrieving',url)
print('Count:',count)
print('Sum:',sum)