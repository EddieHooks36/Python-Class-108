from flask import Flask
from data import me

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

app.run(debug=True)