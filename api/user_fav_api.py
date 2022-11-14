import json
from flask_cors import cross_origin
from flask import request, jsonify
from api import app
from service.user_fav_service import user_fav


@app.route("/api/user/fav", methods=['POST'])
@cross_origin()
def user_fav_api():
    user_id = request.get_json()["userid"]
    # order=request.args.get("order")
    res = user_fav(user_id)
    # print("res",res)
    # print(res)
    return res
