from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import json
base_uri="https://www.imdb.com/search/title/?genres="
rest_uri="&sort=user_rating,desc&title_type=feature&num_votes=25000,"


def user_fav(user_id):
    # fetch fav genre of userid from dataset=genre
    genre="drama"
    # scrap data from https://www.imdb.com/search/title/?genres=drama&sort=user_rating,desc&title_type=feature&num_votes=25000,
    try:
        url=base_uri+genre+rest_uri
        print(url)
        page=requests.get(url)
        # print(page)
        soup=BeautifulSoup(page.text,'html.parser')
        scrap_table_data=soup.find('div',class_="lister list detail sub-list")
        print(scrap_table_data)
    except Exception as e:
        print(e)
    return [];