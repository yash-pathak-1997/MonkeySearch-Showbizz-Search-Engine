from bs4 import BeautifulSoup
import requests
import pandas as pd


def search_click_service(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    scrap_data_movie = soup.find('search-page-result', type='movie').find('ul').find_all('search-page-media-row')
    movie_name = []
    year = []
    cast = []
    image = []
    movie_link = []
    for s in scrap_data_movie:
        y = s.get('releaseyear')  # release year
        year.append(y)
        c = s.get('cast')  # cast of movie
        cast.append(c)
        ds = s.find_all('a', class_="unset")
        p0 = ds[0].find('img')  # image tag of movie
        image.append(p0.get('src'))
        p1 = ds[1].text.strip()  # name of movie
        mlink = ds[1].get('href')
        movie_link.append(mlink)
        movie_name.append(p1)

    # preprocess cast
    print(cast)
    f_cast = list()
    for entry in cast:
        f_cast.append(str(entry).split(","))

    print(type(image))
    print(image)

    data = pd.DataFrame()
    data['mname'] = movie_name
    data['year'] = year
    data['cast'] = f_cast
    data['image'] = image
    data['mlink'] = movie_link
    data.to_csv('rotten_tomatoes_searchurl.csv', index=False)
    js = data.to_json(orient="records")
    print(js)
    return js
