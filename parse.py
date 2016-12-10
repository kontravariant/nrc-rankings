import os
from bs4 import BeautifulSoup as bs
import re
import json
#create holder dictionary for data
dat_dict = {}

#set working directory for html files, open and soupify
wd = os.getcwd()+'/html/'
file_list = os.listdir(wd)
for filename in file_list:
    html_doc = open(wd+filename,'r')
    soup = bs(html_doc, 'html.parser')

    #find table header row and get all column headers into list
    table_head = soup.find('thead').find_all('th')
    heads = [i.get_text() for i in table_head]

    data = []
    table_body = soup.find('tbody').find_next('tbody')
    for row in table_body.find_all('tr'):
        program = [cell for cell in row.find_all('td')][0]
        school = program.find('strong').get_text().replace('tonton','ton')

        school = re.sub(r"([a-z])-([a-z])",r"\1\2",school)
        degree = re.search('><br\/>(.*?)<\/td>',str(program)).group(1)

        row_dat = [cell.get_text() for cell in row.find_all('td')]
        row_dat[0] = school+' ('+degree+')'
        data.append(row_dat)
        if len(row_dat) != len(heads):
            print('unequal)')

    dat_dict['Headers'] = heads
    dat_dict[filename] = data


with open('data.json','w') as f:
   json.dump(dat_dict,f)

