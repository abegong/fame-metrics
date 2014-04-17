import json
import pandas as pd

J = json.loads(file('big-data/fb-export-2013-04-16.json').read())
A = J["answers"]
S = J["sessions"]

names = pd.Series([v['name'] for k,v in S.items()])
platform = pd.Series([v['platform_description'] for k,v in S.items()])

a_sessions = pd.Series([v["session_name"] for k,v in A.items()])
