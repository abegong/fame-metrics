import pandas as pd
import random
import datetime

def Q(df):
	I = list(df.index)
	random.shuffle(I)

	correct_id = I[0]
	confounder_ids = I[1:5]

	name = df.name[I[0]]
	answers = list(enumerate(df.summary[I[:5]]))

	random.shuffle(answers)
	print name
	print '\n'.join(['\t('+str(i+1)+') '+answer for i,(true_index, answer) in enumerate(answers)])

	choice = raw_input()
	choice_id = int(choice)-1

	answer_id = I[answers[choice_id][0]]
	correct = correct_id==answer_id

	if correct:
		print '>>> Correct! <<<'
	else:
		print 'XXX Wrong XXX'

	return {
		'timestamp' : datetime.datetime.now(),
		#User_id
		'correct_id' : correct_id,
		'confounder_ids' : confounder_ids, 
		'answer_id' : answer_id,
		'correct' : correct,
	}

D = pd.read_csv("data/famous-people-FINAL.csv")
E = D.sort('wikipedia_count')[-1000:]

while 1:
	print Q(E)