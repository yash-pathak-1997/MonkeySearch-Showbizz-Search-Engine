import pymongo


def user_fav_dao(user_id):
    # in_res = dict()
    # in_res["UserId"] = user_id
    # in_res["MovieName"] = res["title"]
    # in_res["Language"] = res["OriginalLanguage"]
    # in_res["Genre"] = res["Genre"]

    myclient = pymongo.MongoClient("mongodb+srv://temp:temp@cluster0.fqaslcz.mongodb.net/mernapp?retryWrites=true&w"
                                   "=majority")
    db = myclient.mernapp
    collection = db.SearchClick
    print(user_id)
#     return collection.find({
#  "UserId" : str(user_id)
# },{
#    "Genre": 1
# }
# ).limit(1)
    return collection.aggregate(
        # Lets find our records
        {"$match":{"UserId":str(user_id)}},

        # Now lets group on the name counting how many grouped documents we have
        {"$group":{"_id":"$Genre", "sum":{"$sum":1}}}
    ).limit(1)