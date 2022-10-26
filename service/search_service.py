from bs4 import BeautifulSoup
import requests
import pandas as pd
import json

list_type=['movie','tv']
list_type2=['celebrity','franchise']


def search_service(keyw, filter_data):
    result_data=pd.DataFrame()
    if f'{filter_data["type"]}' == '':
        for i in list_type:
            data=search_data(keyw,i)
            result_data=pd.concat([result_data,data.head(3)],ignore_index=True)
        for i in list_type2:
            data = search_celebrity(keyw,i)
            result_data = pd.concat([result_data, data.head(3)], ignore_index=True)


    else:
        data= search_data(keyw,f'{filter_data["type"]}')
        # print("search_services")
        # print(result_data)
        result_data=data
        # print(result_data)
    print(len(result_data))
    return json.loads(result_data.to_json(orient="records"))


def search_celebrity(keyw,category):
    url = f"https://www.rottentomatoes.com/search?search={keyw}"
    # print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    scrap_data_movie = soup.find('search-page-result', type=f'{category}').find('ul').find_all('search-page-item-row')
    print("scrapdata", scrap_data_movie)
    movie_name = []
    year = []
    cast = []
    image = []
    movie_link = []

    for s in scrap_data_movie:
        y = s.get('releaseyear')  # release year
        print(y)
        if y is None or y.isspace() or not y:
            y = 'NA'
        year.append(y)
        c = s.get('cast')  # cast of movie
        if c is None or c.isspace() or not c:
            c = 'NA'
        cast.append(c)
        ds = s.find_all('a', class_="unset")
        p0 = ds[0].find('img')  # image tag of movie
        img = p0.get('src')
        if img is None or img.isspace() or not img:
            img = 'NA'
        image.append(img)
        p1 = ds[1].text.strip()  # name of movie
        mlink = ds[1].get('href')
        if mlink is None or mlink.isspace() or not mlink:
            mlink = 'NA'
        movie_link.append(mlink)
        if p1 is None or p1.isspace() or not p1:
            p1 = 'NA'
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
    # print("data head 3",data.head(3))
    return data
    # data.to_csv('rotten_tomatoes_searchurl.csv', index=False)
    # js = data.to_json(orient="records")
    # print(js)
    # return js

def search_data(keyw,category):
    url = f"https://www.rottentomatoes.com/search?search={keyw}"
    # print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    scrap_data_movie = soup.find('search-page-result', type=f'{category}').find('ul').find_all('search-page-media-row')
    print("scrapdata",scrap_data_movie)
    movie_name = []
    year = []
    cast = []
    image = []
    movie_link = []

    for s in scrap_data_movie:
        y = s.get('releaseyear')  # release year
        if y is None or y.isspace() or not y:
            y='NA'
        year.append(y)
        c = s.get('cast')  # cast of movie
        if c is None or c.isspace() or not c:
            c='NA'
        cast.append(c)
        ds = s.find_all('a', class_="unset")
        p0 = ds[0].find('img')  # image tag of movie
        img=p0.get('src')
        if img is None or img.isspace() or not img:
            img='NA'
        image.append(img)
        p1 = ds[1].text.strip()  # name of movie
        mlink = ds[1].get('href')
        if mlink is None or mlink.isspace() or not mlink:
            mlink='NA'
        movie_link.append(mlink)
        if p1 is None or p1.isspace() or not p1:
            p1='NA'
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
    # print("data head 3",data.head(3))
    return data
    # data.to_csv('rotten_tomatoes_searchurl.csv', index=False)
    # js = data.to_json(orient="records")
    # print(js)
    # return js

