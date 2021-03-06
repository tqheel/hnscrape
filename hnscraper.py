# for py 2.7
import mechanize
from BeautifulSoup import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders=[('User-agent','chrome')]

query = "http://news.ycombinator.com"

html = br.open(query).read()

soup = BeautifulSoup(html)

rows = soup.findAll('tr',attrs={'class':'athing'})

row_soup = BeautifulSoup(str(rows))

titles = row_soup.findAll('td',attrs={'class':'title'})

title_soup = BeautifulSoup(str(titles))

links = title_soup.findAll('a')

doc_start = '<!DOCTYPE html><html><body><div style="padding: 20px;">'
doc_end = '</div></body></html>'
document = open('hn.html', 'w')
document.truncate()
document.write(doc_start)
document.write('\n')
for i in range(0,9):
	print links[i]
	document.write(str(links[i]))
	document.write('<br/>')
document.write(doc_end)
document.close()
