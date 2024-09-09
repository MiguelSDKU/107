from flask import Flask, request
import json
from config import db


app = Flask(__name__)

products=[]

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

@app.get("/api/products")
def read_products():
  return json.dumps(products) 

@app.post("/api/products")
def saveProducts():
  item = request.get_json()
  # products.append(item )
  db.products.insert_one(item)
  print(item)
  return json.dumps(item)

@app.put("/api/products/<int:index>")
def update_products(index):
  update_item= request.get_json()
  if 0<=index<len(products):
    products[index]=update_item
    return json.dumps(update_item)
  else:
    return "That index does not exist"
  

app.run(debug=True)