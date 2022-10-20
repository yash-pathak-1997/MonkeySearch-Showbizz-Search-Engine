from flask_cors import cross_origin
from api import app


@app.route("/api/login", methods=['GET'])
@cross_origin()
def signin_api():
    return str("Hello world")
