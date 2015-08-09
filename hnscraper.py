# for py 2.7
import mechanize
from BeautifulSoup import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders=[('User-agent','chrome')]

query = "http://news.ycombinator.com"

htmltext = br.open(query).read()

#print htmltext

soup = BeautifulSoup(htmltext)

rows = soup.findAll('tr',attrs={'class':'athing'})

rowSoup = BeautifulSoup(str(rows))

titles = rowSoup.findAll('td',attrs={'class':'title'})

titleSoup = BeautifulSoup(str(titles))

links = titleSoup.findAll('a')

docStart = '<!DOCTYPE html><html><body><div style="padding: 20px;">'
docEnd = '</div></body></html>'
document = open('hn.html', 'w')
document.truncate()
document.write(docStart)
document.write('\n')
for i in range(0,9):
	#print links[i].contents
	print links[i]
	document.write(str(links[i]))
	document.write('<br/>')
document.write(docEnd)
document.close()
