from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import json

base_uri = "https://www.imdb.com/chart/top/"


def top_250_service(sort_by, order):
    try:
        url = base_uri + "?sort=" + sort_by + "," + order + "&mode=simple&page=1"
        print(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        scrap_table = soup.find('tbody', class_="lister-list").find_all('tr')
        links = []
        movies = []
        rates = []
        years = []
        for s in scrap_table:
            links.append(s.find('td', class_='titleColumn').find_all('a',
                                                                     attrs={'href': re.compile("^/title/")}))
            movies.append(s.find('td', class_='titleColumn').a.text)
            rates.append(s.find('td', class_='ratingColumn').text.replace('\n', ""))
            years.append(s.find('span', class_='secondaryInfo').text.replace('(', "").replace(')', ''))

        data = pd.DataFrame()
        data['movies'] = movies
        data['rating'] = rates
        data['year'] = years
        link_title = []
        scrap_movies = soup.find_all('td', class_='titleColumn')
        img_src = []
        for link in scrap_movies:
            p = s.find('a', attrs={'href': re.compile("^/title/")})
            i = s.find('img')
            link_title.append(p.get('href'))
            img_src.append(i.get('src'))

        data['alink'] = link_title
        data['imgsrc'] = img_src
        return json.loads(data.to_json(orient="records"))
    except Exception as e:
        print(e)
