import json
import pandas as pd

with open('data.json','r+') as f:
    data = json.load(f)

dat = {}
keys = [key for key in data.keys() if not key=='Headers']
for key in keys:
    dat[key] = pd.DataFrame(data[key],columns=data['Headers'])

writer = pd.ExcelWriter('nrc_dat.xlsx', engine='xlsxwriter')
for key, frame in dat.items():
    key = key[:30].replace('.txt','')
    frame.to_excel(writer,sheet_name=key)
writer.save()
