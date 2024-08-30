import requests
from bs4 import BeautifulSoup
import fake_useragent
from time import sleep
import json

user=fake_useragent.UserAgent().random

headers={'User-Agent': user}


#data={}
#url="https://shop.kerama-marazzi.ru/"
#responce=requests.get(url,headers=headers)
#soup=BeautifulSoup(responce.text,'lxml')
#tov_name=soup.find('ul', class_="accordion-menu").find_all('li', class_="has-child")
#for cat in tov_name:
    #name=cat.find('a').text.strip()
    #vse_tov=cat.find('ul', class_="child collapse").find_all

    #url="https://shop.kerama-marazzi.ru"+ cat.find('a').get('href')
    #data[name]=url



#with open('data/category_url.json','a',encoding='utf8') as file:
    #for key, value in data.items():
    #json.dump(data,file,indent=4,ensure_ascii=False)
        #(f'{key}, {value}\n')


with open('data/category_url.json','r',encoding='utf8') as f:
    category=json.load(f)

for name,url in category.items():
    responce=requests.get(url,headers=headers)
    soup=BeautifulSoup(responce.text,'lxml')
    pagination=soup.find('ul', class_="pagination justify-content-center")
    if pagination not 








    #lines=[lines.strip() for lines in file.readlines()]

#print(lines)


#def get_url(url):
    #responce=requests.get(line,headers=headers)
    #soup=BeautifulSoup(responce.text,'lxml')
    #return soup
