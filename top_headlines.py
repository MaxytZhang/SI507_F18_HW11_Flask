from flask import Flask, render_template
import requests
import json
import secret
import time

app = Flask(__name__)

h = time.localtime()[3]
greet = "Hello,"
if 19 < h < 24:
    greet = "Good night"
elif 15 < h < 20:
    greet = "Good evening"
elif 11 < h < 16:
    greet = "Good afternoon"
else:
    greet = "Good morning"

@app.route('/')
def index():
    return '<h1>Welcome!</h1>'


@app.route('/user/<nm>')
def userTech(nm):
    key = secret.api_key
    url = "https://api.nytimes.com/svc/topstories/v2/technology.json"
    pd = {
        'api-key': key,
        'callback': "5"
    }
    response = requests.get(url, params=pd).text
    results = json.loads(response)
    headers = []
    count = 0
    for result in results["results"]:
        count += 1
        i = str(count) + ". " + result["title"] + " (" + result["url"] + ")"
        headers.append(i)
        if count == 5:
            break
    return render_template('user.html', greet=greet, name=nm, items=headers, section="technology")

@app.route('/user/<nm>/<section>')
def userSection(nm, section):
    key = secret.api_key
    url = "https://api.nytimes.com/svc/topstories/v2/{}.json".format(section)
    pd = {
        'api-key': key,
        'callback': "5"
    }
    response = requests.get(url, params=pd).text
    results = json.loads(response)
    headers = []
    count = 0
    for result in results["results"]:
        count += 1
        i = str(count) + ". " + result["title"] + " (" + result["url"] + ")"
        headers.append(i)
        if count == 5:
            break
    return render_template('user.html', greet=greet, name=nm, items=headers, section=section)

if __name__ == '__main__':  
    print('starting Flask app', app.name)
    app.run(debug=True)