import json
from flask_cors import cross_origin
from flask import request, jsonify
from api import app
from service.user_fav_service import user_fav_service


@app.route("/api/user/fav", methods=['POST'])
@cross_origin()
def user_fav_api():
    user_id = request.args.get("userid")
    res = user_fav_service(user_id)
    return res
