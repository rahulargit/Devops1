from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import urllib.parse
import pymongo
from bson.json_util import dumps





from pymongo.mongo_client import MongoClient

load_dotenv()
username=os.getenv("Mongo_USERNAME")
password=os.getenv("Mongo_password")
#print(f"username:{username}")
#print(password)
#MONGO_URI=os.getenv("MONGO_URI")
username=urllib.parse.quote_plus(username) 
password = urllib.parse.quote_plus(password)
print(password)

MONGO_URI = f"mongodb+srv://{username}:{password}@cluster0.zagyrwe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

uri = MONGO_URI
print(uri)

# Create a new client and connect to the server
client = MongoClient(uri)

db=client.test

collection=db['flask_tutorial']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


app=Flask(__name__)



@app.route('/submit',methods=['POST'])
def submit():
    form_data=dict(request.json)
    email=request.form.get('EMAIL')
    password=request.form.get('Password')
    collection.insert_one(form_data)
    print(form_data)
    print(email)
    print(password)

    return dumps(form_data)


@app.route('/view')
def view():
    data=collection.find()

    data=list(data)
    data={
        'data':data
    }
    print([dumps(data)])
    return dumps(data)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=9000,debug=True)