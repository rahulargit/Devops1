from flask import Flask, request, render_template
from datetime import datetime
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
print(password)
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

@app.route('/')

def home():
    day_of_week=datetime.now().strftime('%A')
    current_time=datetime.now().strftime('%H:%M:%S')
    return render_template('index.html',day_of_week=day_of_week,current_time=current_time)

@app.route('/second')

def second():
    return 'This is the second part of the flask it is the /second route'

@app.route('/third/<name>')
def third(name):
    print(name)
    return 'this is the third api'


@app.route('/api')
def name():
    name=request.values.get('name')
    age=request.values.get('age')
    return 'Hii your name is '+name+'and your age is '+age


@app.route('/submit',methods=['POST'])
def submit():
    form_data=dict(request.form)
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
    #print(data)
    return dumps(data)

if __name__=='__main__':
    app.run(debug=True)