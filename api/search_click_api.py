from flask_cors import cross_origin
from flask import request
from api import app
from service.search_click_service import search_click_service


@app.route("/api/search_click", methods=['POST'])
@cross_origin()
def search_click_api():
    url = request.get_json()
    res = search_click_service(url["url"])
    return res
