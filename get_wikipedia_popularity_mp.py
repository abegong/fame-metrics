import pandas as pd
import urllib
import requests
from lxml import html
import re
import json
import multiprocessing

def get_pop((i,name)):
	try:
		r = requests.get('http://stats.grok.se/en/latest90/'+urllib.quote(name), timeout=5)
		h = html.fromstring(r.content)
		e = h.xpath('//p[1]')[0]

		wikipedia_name = e.xpath('a/text()')[0]
		wikipedia_link = e.xpath('a/@href')[0]
		wikipedia_count = int(re.findall('viewed (\d+)\n', e.text_content())[0])

		print i, name
		return {
			'index': int(i),
			'name': name,
			'wikipedia_name' : wikipedia_name,
			'wikipedia_link' : wikipedia_link,
			'wikipedia_count' : wikipedia_count,
		}

	except requests.exceptions.Timeout:
		print i, '!!!', name
		return None


DF = pd.read_csv("./famous_people.csv")
fetch_list = [(i,name) for i, (name, _, _, _, _) in list(DF.iterrows())[20000:30000]]

# A = pd.read_csv("./famous_people.csv")
# B = pd.DataFrame([json.loads(l) for l in file('./wikipedia_popularity.jl', 'r').read().splitlines()])
# missing = set(A.index).difference(B["index"])
# C = A.ix[missing]
# fetch_list = [(i,name) for i, (name, _, _, _, _) in list(C.iterrows())]

pool = multiprocessing.Pool(20)
results = pool.map(get_pop, fetch_list)
print sum([r==None for r in results])*1./len(results), "percent complete"


outfile = file('wikipedia_popularity.jl', 'ab')
for r in results:
	if r != None:
		outfile.write(json.dumps(r)+'\n')
outfile.close()