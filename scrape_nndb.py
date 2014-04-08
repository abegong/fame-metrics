import requests
from lxml import html
import pandas as pd

letter_urls = [
	'http://www.nndb.com/lists/493/000063304/',
	'http://www.nndb.com/lists/494/000063305/',
	'http://www.nndb.com/lists/495/000063306/',
	'http://www.nndb.com/lists/496/000063307/',
	'http://www.nndb.com/lists/497/000063308/',
	'http://www.nndb.com/lists/498/000063309/',
	'http://www.nndb.com/lists/499/000063310/',
	'http://www.nndb.com/lists/500/000063311/',
	'http://www.nndb.com/lists/501/000063312/',
	'http://www.nndb.com/lists/502/000063313/',
	'http://www.nndb.com/lists/503/000063314/',
	'http://www.nndb.com/lists/504/000063315/',
	'http://www.nndb.com/lists/505/000063316/',
	'http://www.nndb.com/lists/506/000063317/',
	'http://www.nndb.com/lists/507/000063318/',
	'http://www.nndb.com/lists/508/000063319/',
	'http://www.nndb.com/lists/509/000063320/',
	'http://www.nndb.com/lists/510/000063321/',
	'http://www.nndb.com/lists/511/000063322/',
	'http://www.nndb.com/lists/512/000063323/',
	'http://www.nndb.com/lists/513/000063324/',
	'http://www.nndb.com/lists/514/000063325/',
	'http://www.nndb.com/lists/515/000063326/',
	'http://www.nndb.com/lists/516/000063327/',
	'http://www.nndb.com/lists/517/000063328/',
	'http://www.nndb.com/lists/518/000063329/',
]

info = []

for url in letter_urls:
	print url

	R = requests.get(url)
	H = html.fromstring(R.content)

	names = H.xpath('//table/tr/td[1]/a/text()')
	occupations = H.xpath('//table/tr/td[2]/font/text()')
	summaries = [e.text_content() for e in H.xpath('//table/tr/td[3]')]
	# summaries = H.xpath('//table/tr/td[3]/font/text()')
	birthdays = H.xpath('//table/tr/td[4]/tt/text()')
	deathdays = H.xpath('//table/tr/td[5]/tt/text()')

	print len(names),
	print len(occupations),
	print len(summaries),
	print len(birthdays),
	print len(deathdays),
	print

	info = info+zip( names, occupations, summaries, birthdays, deathdays )

DF = pd.DataFrame(info, columns=["name", "occupation", "summary", "birthday", "deathday"])
DF.to_csv("famous_people.csv", index=False)
