import json
from flask_cors import cross_origin
from flask import request, jsonify
from api import app
from service.top_250 import top_250


@app.route("/api/top/250", methods=['GET'])
@cross_origin()
def top_250_api():
    sortby = request.args.get("sort")
    order=request.args.get("order")
    res = top_250(sortby,order)
    # print(res)
    return res
