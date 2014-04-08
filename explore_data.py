import pandas as pd
import pylab as plt

A = pd.read_csv("data/famous_people.csv")

#How many people in each occupation?
x = A.occupation.value_counts()
print x.to_string
print x[x>100].sum()*1./x.sum()
print x[x>500].sum()*1./x.sum()

#Natural categories for occupations?

#How many people in each categories?
#Average fame by birthday?
#Average fame by category?
#Fame deciles by category?
