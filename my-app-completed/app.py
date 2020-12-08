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

    apikey = 'abcde' # change to your own apikey from fix.io
    endpoint = "http://data.fixer.io/api/latest?access_key=" + apikey

    data = {}
    with urllib.request.urlopen(endpoint) as url:
        response = json.loads(url.read().decode())
        # print(response["rates"])

        # Calculating exchange amount for various currency
        hkd =  amount * response["rates"]["HKD"] / response["rates"]["USD"]
        cny =  amount * response["rates"]["CNY"] / response["rates"]["USD"]

        # Preparing Data to Pass to render_template()
        data = {
        "amount": amount,
        "hkd": hkd,
        "cny": cny
        }
        print(data)

    return render_template('result.html', data=data)
