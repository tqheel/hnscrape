# for py 3.4
#import mechanize
from bs4 import BeautifulSoup
import requests

url = "http://news.ycombinator.com"

request = requests.get(url)

soup = BeautifulSoup(request.text, "html.parser")

rows = soup.findAll('tr',attrs={'class':'athing'})

row_soup = BeautifulSoup(str(rows), "html.parser")

titles = row_soup.findAll('td',attrs={'class':'title'})

title_soup = BeautifulSoup(str(titles), "html.parser")

links = title_soup.findAll('a')

doc_start = '<!DOCTYPE html><html><body><div style="padding: 20px;"><ol>'
doc_end = '</div></body></html>'
document = open('hn.html', 'w')
document.truncate()
document.write(doc_start)
document.write('\n')
for i in range(0,10):
	print (str(links[i]).encode('UTF-8'))
	document.write('<li>'+str(links[i])+'</li>')
	document.write('<br/>')
document.write(doc_end)
document.close()
