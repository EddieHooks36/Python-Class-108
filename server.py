from flask import Flask, abort, request
from data import me, mock_catelog
from config import db
from bson import ObjectId

import json
from flask_cors import CORS

app = Flask(__name__) # similar to new task in JS/create a new instance
CORS(app)

@app.get("/")
def home():
    return "Hi my name is..."


@app.get("/about")
def about():
    return "Eddie"


@app.get("/contact/me")
def contact_me():
    return "eddie@something.com"


################################################################
###########API -> JSON #########################################
################################################################

@app.get("/api/developer")
def developer():
    return json.dumps(me) # parse me into a json string


@app.get("/api/developer/address")
def address():
    address = me["address"]
    # return address["street"] + " # " + str(address["number"]) + address["city"] + address["zip"]
    # f string
    return f'{address["street"]} #{address["number"]}, {address["city"]}, {address["zip"]}'


def fix_id(obj):
    obj["_id"] = str(obj["_id"])

@app.get("/api/catelog")
def the_catelog():
    cursor = db.product.find({})
    results = []
    for prod in cursor:
        fix_id(prod)
        results.append(prod)

    return json.dumps(results)


@app.post("/api/catelog")
def save_product():
    data = request.get_json()
    db.product.insert_one(data)
    fix_id(data)
    # print("-" * 25)
    # print(data)

    return json.dumps(data)


@app.get("/api/catelog/count")
def product_count():
    total = db.product.count_documents({})
    return json.dumps(total)


@app.get("/api/category/<cat>")
def prods_by_category(cat):
    cursor = db.product.find({"category" : cat})
    results = []
    for prod in cursor:
        fix_id(prod)
        results.append(prod)

    return json.dumps(results)


@app.get("/api/product/<id>")
def prod_by_id(id):
    _id = ObjectId(id)
    prod = db.product.find_one({"_id" : _id})
    if prod is None:
        return abort(404) # Not Found
    
    fix_id(prod)
    return json.dumps(prod)


@app.get("/api/product/search/<text>")
def prod_title(text):
      cursor = db.product.find({"title" : {"$regex" : text, "$options" : "i"}})
      results = []
      for prod in cursor:
          fix_id(prod)
          results.append(prod)
    #   for prod in mock_catelog:
    #     if text.lower() in prod["title"].lower:
    #         results.append(prod)

      return json.dumps(results)


@app.get("/api/categories")
def get_categories():
    cursor = db.product.distinct("category")
    # for prod in mock_catelog:
    #     cat  = prod["category"]
    #     if cat not in results:
    #         results.append(cat)

    return json.dumps(list(cursor))



@app.get("/api/total")
def get_total():
    total = 0
    for prod in mock_catelog:
        total += prod["price"]

    return json.dumps(total)


@app.get("/api/cheaper/<price>")
def get_cheaper(price):
    price = float(price)
    results = []
    for prod in mock_catelog:
        if prod["price"] <= price:
            results.append(prod)

    return json.dumps(results)


app.run(debug=True)