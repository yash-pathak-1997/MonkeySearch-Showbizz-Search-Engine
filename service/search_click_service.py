from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
from dao.search_click_dao import search_click_dao


def search_click_service(url):
    # url = "https://www.rottentomatoes.com/m/abcd_any_body_can_dance"
    print(url)
    page = requests.get(url)
    print(page)
    soup = BeautifulSoup(page.text, 'html.parser')
    # print(soup.prettify())
    scrap_data_movie = soup.find('div', id='mainColumn')
    # .find('ul').find_all('search-page-item-row')
    # print(scrap_data_movie)
    list = dict()
    image = scrap_data_movie.find('div', class_='thumbnail-scoreboard-wrap').find('div',
                                                                                  class_='movie-thumbnail-wrap').div.img
    image = image.get('src')  # poster link
    list['poster'] = image
    header = scrap_data_movie.find('score-board', class_='scoreboard')
    title = header.find('h1', class_="scoreboard__title").text  # title of movie
    # print(header)
    info = header.find('p', class_="scoreboard__info").text.split(',')
    length = len(info)
    year = ""
    zoner = ""
    time = ""
    if length > 0:
        year = info[0]
    if length > 1:
        zoner = info[1]
    if length > 2:
        time = info[2]
    list['title'] = title
    list['year'] = year
    list['zoner'] = zoner
    list['time'] = time
    print(title, year, zoner, time)
    print(image)

    movie_info = scrap_data_movie.find('div', id='movieSynopsis').text.strip()
    print(movie_info)  # about movie
    list['info'] = movie_info
    meta_data = scrap_data_movie.find('ul', class_='info').find_all('li')
    # print(meta_data)
    for r in meta_data:
        key = r.find('div', class_='meta-label').text.strip()
        value = r.find('div', class_='meta-value').text.strip().replace("\n", '').replace(" ", '')
        list[key.replace(":", "").replace(" ", "")] = value
        # print(key,value)
    # print(list)
    return json.loads(json.dumps(list))
