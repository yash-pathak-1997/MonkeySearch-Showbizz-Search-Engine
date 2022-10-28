from flask import Flask

app = Flask(__name__)

from api import search_api
from api import search_click_api
from api import search_enter_api
from api import coming_soon_api
