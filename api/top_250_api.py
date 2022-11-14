import json
from flask_cors import cross_origin
from flask import request, jsonify
from api import app
from service.top_250 import top_250


@app.route("/api/top/250", methods=['GET'])
@cross_origin()
def top_250_api():
    sortby = request.get_json()["sort"]
    order = request.get_json()["order"]
    res = top_250(sortby,order)
    # print(res)
    return res
