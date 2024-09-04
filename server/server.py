from flask import Flask 
import json


app = Flask(__name__)

@app.get("/")
def home():
  return "hello from flask"

@app.get("/about")
def about():
    me = {"name":"Mikee"}
    return json.dumps(me)
  
#create an API to footer that contains the name of the page (organika)
@app.get("/footer")
def footer():
  pageName={"pageName":"organika"}
  return json.dumps(pageName)

app.run(debug=True)