from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':  
    print('starting Flask app', app.name)
    app.run(debug=True)