import pandas as pd
pd.read_csv(data_path+"gform-surveys/Getting stuff done (Responses) - Form Responses.csv")
A = pd.read_csv("./famous_people.csv")
list(A)
A.occupation.value_counts()
A[A.occupation=='Stamp Collector']
A.occupation.value_counts().value_counts().hist()
import pylab as plt
plt.show()
A.occupation.value_counts().hist()
plt.show()
x = A.occupation.value_counts()
x[x>100]
x[x>100].sum()
x[x>100].sum()*1./x.xum()
x[x>100].sum()*1./x.sum()
x[x>500].sum()*1./x.sum()
