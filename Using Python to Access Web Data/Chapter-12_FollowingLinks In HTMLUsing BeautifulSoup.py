import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
if len(url)<1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Carey.html'

n=0
Sequence = ''
names = []
i=int(input('Enter count:'))
j=int(input('Enter position:'))
while n<i:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
    tags = soup('a')
    Sequence = Sequence +' '+ tags[j-1].text
    names.append(tags[j-1].text)
    url = tags[j-1].get('href', None)
    print('Retrieving:',url)
    n=n+1
# print('Sequence of names:',Sequence)
# print('Last name in sequence:',names[-1])