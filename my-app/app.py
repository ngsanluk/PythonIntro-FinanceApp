from flask import Flask
from flask import render_template
from flask import request
import urllib, json

app = Flask(__name__)

# index/home page
@app.route('/')
def index():
    return render_template('index.html')

# currency exchange result page
@app.route('/result', methods=['POST'])
def result():
    amount = float(request.form['amount'])

    apikey = 'PutYourKeyHere'
    endpoint = "http://data.fixer.io/api/latest?access_key=" + apikey
    print("endpoint -> ")
    print(endpoint)

    data = {}
    with urllib.request.urlopen(endpoint) as url:
        response = json.loads(url.read().decode())

        print(response)
        # print(response["rates"])
        # print(response["rates"]["HKD"])

        # Calculating exchange amount for various currency


        # Preparing Data to Pass to render_template()
        data = {
        "amount": amount,
        "hkd": 1111, # put hkd amount here
        "cny": 2222 # put cny ammout here. or add more currency e.g. JPY
        }
        print(data)

    return render_template('result.html', data=data)
