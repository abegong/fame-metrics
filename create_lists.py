import pandas as pd
import json
import re
import dateutil

def convert_df_to_list(df, filename=None):
	celeb_list = []

	for i, row in df.iterrows():
		celeb_list.append({
			"index": row["index"],
			"name": row["name"],
			"tags": [row.summary],
		})

	if filename:
		file(filename, 'w').write('\n'.join([json.dumps(j) for j in celeb_list]))

	return celeb_list

def try_parse_birthyear(x):
	if x == '?':
		return None

	#'c. XXX...'
	matches = re.findall('c\. (\d+)( BC)?', x)
	if len(matches) > 0:
		if matches[0][1] == '':
			return int(matches[0][0])
		else:
			#For BC years
			return -1*int(matches[0][0])

	#'XXX BC'
	matches = re.findall('(\d+) BC', x)
	if len(matches) > 0:
		#For BC years
		return -1*int(matches[0][0])

	#'fl. X[st|th|nd...] c. BC'
	matches = re.findall('fl\.? (\d).. c. BC', x)
	if len(matches) > 0:
		#For BC years
		return -100*int(matches[0][0])

	#'fl. X[st|th|nd...] c. AD'
	matches = re.findall('fl\.? (\d+).. c. AD', x)
	if len(matches) > 0:
		#For BC years
		return 100*int(matches[0][0])

	try:
		date = dateutil.parser.parse(x)
		return date.year
	except:
		print x
		return None


D = pd.read_csv('data/famous-people-FINAL.csv')
D["fame"] = D.wikipedia_count
D["birthyear"] = D.birthday.map(try_parse_birthyear)

C = pd.read_csv('data/category-mappings.csv')
C["category"] = C["Unnamed: 0"]

if 0:
	pol_categories = list(C.category[C.Politics==1])
	politics_df = D[D.occupation.map( lambda x: x in pol_categories ) & (D.fame>100000)]
	convert_df_to_list(politics_df, 'data/lists/politics.jl')

	sci_categories = list(C.category[C.Science==1])
	sci_df = D[D.occupation.map( lambda x: x in sci_categories ) & (D.fame>20000)]
	convert_df_to_list(sci_df, 'data/lists/science.jl')

	sports_categories = list(C.category[C.Sports==1])
	sports_df = D[D.occupation.map( lambda x: x in sports_categories ) & (D.fame>100000)]
	convert_df_to_list(sports_df, 'data/lists/sports.jl')

	history_df = D[(D.birthyear < 1900) & (D.fame>100000)]
	convert_df_to_list(history_df, 'data/lists/history.jl')

	movie_categories = ['Actor', 'Film Director', 'Film/TV Producer', 'Screenwriter', 'Cinematographer']
	movie_df = D[D.occupation.map( lambda x: x in movie_categories ) & (D.fame>200000)]
	convert_df_to_list(movie_df, 'data/lists/movies.jl')

	generic_df = D[D.occupation.map( lambda x: x in movie_categories ) & (D.fame>300000)]
	convert_df_to_list(generic_df, 'data/lists/generic.jl')
