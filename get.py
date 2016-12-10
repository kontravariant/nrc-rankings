import requests
import os
from bs4 import BeautifulSoup as bs
import json

def get_links():
    url = 'http://www.chronicle.com/article/NRC-Rankings-Overview-/124724/'
    html_doc = requests.get(url)
    soup = bs(html_doc.text, 'html.parser')

    field = soup.find('p').find_next('p')
    link_list = field.find_next('blockquote')
    links = [a['href'] for a in link_list.find_all('a',href=True)]
    link_names = [i.get_text() for i in link_list.find_all('a')]
    link_dict = dict(zip(link_names,links))
    print(link_dict)
    return(link_dict)

def write_html(link_dict):
    for cat, link in link_dict.items():
        cat_html = requests.get(link)
        cat = cat.replace(', ','_').replace(' ','_').replace('/','_')
        fn = '/html/'+cat+'.txt'
        cwd = os.getcwd()
        fpath = cwd+fn
        with open(fpath,'w') as f:
            f.write(cat_html.text)

links = get_links()
with open('link_list.json','w') as f:
    json.dump(links,f)
#write_html(links)

