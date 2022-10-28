from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import json
base_uri="https://www.imdb.com/chart/top/"


def top_250(sortby,order):
    try:
        url=base_uri+"?sort="+sortby+","+order+"&mode=simple&page=1"
        print(url)
        page=requests.get(url)
        # print(page)
        soup=BeautifulSoup(page.text,'html.parser')
        # print(soup.prettify())
        scrap_table=soup.find('tbody',class_="lister-list").find_all('tr')
        # print(len(scrap_table))
        links=[]
        movies=[]
        rates=[]
        years=[]
        for s in scrap_table:
            links.append(s.find('td',class_='titleColumn').find_all('a',
                                  attrs={'href': re.compile("^/title/")}))
            movies.append(s.find('td',class_='titleColumn').a.text)
            rates.append(s.find('td',class_='ratingColumn').text.replace('\n',""))
            years.append(s.find('span',class_='secondaryInfo').text.replace('(',"").replace(')',''))

        # print(movies)
        # print(links)
        # print(rates)
        # print(years)

        data=pd.DataFrame()
        data['movies']=movies
        data['rating']=rates
        data['year']=years
        link_title=[]
        scrap_movies=soup.find_all('td',class_='titleColumn')
        # print("length",len(scrap_movies))
        # print(scrap_movies)
        img_src=[]
        for link in scrap_movies:
            p=s.find('a',attrs={'href': re.compile("^/title/")})
            i=s.find('img')
            # display the actual urls
            # print(p.get('href'))
            # print(i.get('src'))
            # print(link.get('href'))
            link_title.append(p.get('href'))
            img_src.append(i.get('src'))

        # print(len(link_title))
        data['alink']=link_title
        data['imgsrc']=img_src
        return json.loads(data.to_json(orient="records"))
    except Exception as e:
        print(e)