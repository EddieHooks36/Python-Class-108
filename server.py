from flask import Flask, abort
from data import me, mock_catelog

import json

app = Flask(__name__) # similar to new task in JS/create a new instance


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


@app.get("/api/catelog")
def the_catelog():
    return json.dumps(mock_catelog)


@app.get("/api/catelog/count")
def product_count():
    count = len(mock_catelog)
    return json.dumps(count)


@app.get("/api/category/<cat>")
def prods_by_category(cat):
    results = []
    for prod in mock_catelog:
        if prod["category"] == cat:
            results.append(prod)


    return json.dumps(results)


@app.get("/api/product/<id>")
def prod_by_id(id):
    for prod in mock_catelog:
        if prod["_id"] == id:
          return json.dumps(id)


    return abort(404) # Not Found


@app.get("/api/product/search/<text>")
def prod_title(text):
      results = []
      for prod in mock_catelog:
        if text.lower() in prod["title"].lower:
            results.append(prod)

      return json.dumps(results)


@app.get("/api/categories")
def get_categories():
    results = []
    for prod in mock_catelog:
        cat  = prod["category"]
        




app.run(debug=True)