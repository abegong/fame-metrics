import pandas as pd
import urllib
import requests
from lxml import html
import re
import json

DF = pd.read_csv("data/famous_people.csv")

for i, (name, _, _, _, _) in list(DF.iterrows())[16890:]:
	try:
		print i, name

		r = requests.get('http://stats.grok.se/en/latest90/'+urllib.quote(name), timeout=1)
		h = html.fromstring(r.content)
		e = h.xpath('//p[1]')[0]

		wikipedia_name = e.xpath('a/text()')[0]
		wikipedia_link = e.xpath('a/@href')[0]
		wikipedia_count = int(re.findall('viewed (\d+)\n', e.text_content())[0])

		file('wikipedia_popularity.jl', 'ab').write(json.dumps({
			'index': int(i),
			'name': name,
			'wikipedia_name' : wikipedia_name,
			'wikipedia_link' : wikipedia_link,
			'wikipedia_count' : wikipedia_count,
		})+'\n')

	except requests.exceptions.Timeout:
		print '!'