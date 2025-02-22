from json import dumps
from flask import Flask, request, render_template,jsonify
from datetime import datetime
import requests

Backend_url='http://192.168.1.6:9000'
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
    requests.post(Backend_url+'/submit',json=form_data)
    return 'successfully'


@app.route('/get_data')
def get_data():
    response=requests.get(Backend_url+'/view')
    
    return dumps(response.json())

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)