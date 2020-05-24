import urllib.request, urllib.parse, urllib.error
import ssl
import requests
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location:')
if len(url)<1:
    url = 'http://py4e-data.dr-chuck.net/comments_521899.json'

html = urllib.request.urlopen(url, context=ctx).read().decode('utf-8')
# html = requests.get(url).text

# print(html)
data = json.loads(html)
# print(data)
print('Retrieving',url)
print('Retrieved ',len(html), 'characters')
count = 0
sum = 0
for num in data['comments']:
    # print(num['count'])
    count = count + 1
    sum = sum + num['count']
print('Count:',count)
print('Sum:',sum)