from bs4 import BeautifulSoup
import requests
import pandas as pd


def coming_soon_service(filter_data):
    region = filter_data["region"]
    type_o = filter_data["type"]
    url = f"https://www.imdb.com/calendar/?ref_=rlm&region={region}&type={type_o}"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    articles = soup.find('section', class_='ipc-page-section ipc-page-section--base').find_all('article',
                                                                                               class_="sc-f56042d2-1 kgXUZB")
    res = {}
    movies_list = []
    for u in articles:
        date_html = u.find('div', class_="ipc-title ipc-title--title ipc-title--base ipc-title--on-textPrimary")
        date = date_html.find('hgroup').find('h3', class_="ipc-title__text").text
        movie_list = u.find('ul', class_="ipc-metadata-list ipc-metadata-list--dividers-after sc-f56042d2-2 hgbLIC "
                                         "ipc-metadata-list--base").find_all('li',
                                                                             class_="ipc-metadata-list-summary-item "
                                                                                    "ipc-metadata-list-summary-item"
                                                                                    "--click sc-b4bc18a3-0 ldrlyp")

        for movie in movie_list:
            temp = {}
            movie_name = movie.find('div', class_="ipc-metadata-list-summary-item__tc").find('a', class_="ipc-metadata-list-summary-item__t").text
            if movie.find('img', class_="ipc-image") is None:
                link = "NA"
            else:
                link = movie.find('img', class_="ipc-image").get('src')
            temp["mname"] = movie_name
            temp["imagelink"] = link
            temp["date"] = date
            movies_list.append(temp)

        res["movies"] = movies_list

    return res
