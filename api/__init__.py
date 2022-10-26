from flask import Flask

app = Flask(__name__)

from api import signin_api
from api import search_api
from api import search_click_api
