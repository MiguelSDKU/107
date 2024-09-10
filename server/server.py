# from flask import Flask, request
# import json
# from config import db


# app = Flask(__name__)

# products=[]

# def fix_id(obj):
#   obj["_id"]=str(obj["_id"])
#   return obj

# @app.get("/")
# def home():
#   return "hello from flask"

# @app.get("/about")
# def about():
#     me = {"name":"Mikee"}
#     return json.dumps(me)
  
# #create an API to footer that contains the name of the page (organika)
# @app.get("/footer")
# def footer():
#   pageName={"pageName":"organika"}
#   return json.dumps(pageName)

# @app.get("/api/products")
# def read_products():
#   return json.dumps(products) 

# @app.post("/api/products")
# def saveProducts():
#   item = request.get_json()
#   # products.append(item )
#   db.products.insert_one(item)
#   print(item)
#   return json.dumps(fix_id(item))

# @app.put("/api/products/<int:index>")
# def update_products(index):
#   update_item= request.get_json()
#   if 0<=index<len(products):
#     products[index]=update_item
#     return json.dumps(update_item)
#   else:
#     return "That index does not exist"
  

# app.run(debug=True)

from flask import Flask, request
import json
from config import db

app = Flask(__name__)

def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

@app.get("/")
def home():
    return "Welcome to the Organika API"

@app.get("/api/catalog")
def get_catalog():
    products = list(db.products.find())
    return json.dumps([fix_id(prod) for prod in products])

@app.post("/api/catalog")
def save_product():
    product = request.get_json()
    db.products.insert_one(product)
    return json.dumps(fix_id(product))

@app.get("/api/reports/total")
def total_value():
    products = list(db.products.find())
    total = sum([prod["price"] for prod in products if "price" in prod])
    return json.dumps({"total_value": total})

@app.get("/api/products/<category>")
def get_products_by_category(category):
    products = list(db.products.find({"category": category}))
    return json.dumps([fix_id(prod) for prod in products])

if __name__ == "__main__":
    app.run(debug=True)
