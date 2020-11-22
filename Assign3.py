import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/known_by_Kirsten.html' # raw_input('Enter URL : ')

position = 18 
count = 7

def allerretour(url):
    print('Retrieving: ' + url)
    soup = BeautifulSoup(urllib.request.urlopen(url).read())
    link = list()
    for tag in soup('a'):
        link.append(tag.get('href', None))
    return(link)


for x in range(1, count + 2):
    url = allerretour(url)[position-1]