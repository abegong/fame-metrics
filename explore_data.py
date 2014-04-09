import pandas as pd
import json
import pylab as plt
import random

A = pd.read_csv("data/famous_people.csv")
A["index"] = A.index

B = pd.DataFrame([json.loads(l) for l in file('data/wikipedia_popularity.jl').read().splitlines()])
C = B.drop_duplicates('index')
del(C["name"])
del(C["wikipedia_name"])

D = A.merge(C, on='index')
# D.to_csv('data/famous-people-FINAL.csv', index=False, encoding='utf-8')

#How many people in each occupation?
x = D.occupation.value_counts()
major_occupations = x[:30]
print x.to_string()

# print x[x>100].sum()*1./x.sum()
# print x[x>500].sum()*1./x.sum()

#100 most famous people?
x = list(D.sort('wikipedia_count').name.tail(100))
x.reverse()
print x

# Since this is from the last 90 days, people who released movies, died, etc. during that time have way more hits than you would otherwise expect.
# I am relieved to see Abraham Lincoln, Nelson Mandela, and Albert Einstein all in the top 100.

#Natural categories for occupations?

#How many people in each category?
#Average fame by birthday?
#Average fame by category?
#Fame deciles by category?

D[D.name=="Paul Walker"][["name", "occupation", "summary"]]
#               name occupation                    summary
# 37945  Paul Walker   Business  CEO of The Sage Group plc
# 37946  Paul Walker      Actor           2 Fast 2 Furious


x = D.name.value_counts()
x[x>1]
# Out[79]: 
# John Anderson     4
# Samuel Butler     3
# John Russell      3
# Charlie Wilson    3
# George Miller     3
# James Wilson      3
# Charles Taylor    3
# David Davis       3
# Robert Brown      3
# Jim Davis         3
# John Howard       3
# John Ireland      3
# John Newton       3
# Norman Foster     2
# Dave Stewart      2
# ...
# Hanno                  2
# John Golding           2
# Tom Scott              2
# Craig Thomas           2
# John Milton            2
# Christian Wolff        2
# James Marshall         2
# John Carter            2
# John Fahey             2
# William J. McDonald    2
# Thomas Dekker          2
# John Adams             2
# John W. Brown          2
# Ann Richards           2
# John Holmes            2
# Length: 265, dtype: int64
