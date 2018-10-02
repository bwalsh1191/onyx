import requests
from flask import Flask, render_template, request
import json
import html.parser as htmlparser
from datetime import datetime

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET', 'POST'])
def index():
    parser = htmlparser.HTMLParser()
    new_symbol = 'AAPl'

    if request.method == 'POST':
        new_symbol = request.form.get('symbol')
    
    url = 'https://api.stocktwits.com/api/2/streams/symbol/{}.json'

    stockTwits = requests.get(url.format(new_symbol)).json()
    stockTwits_data = []
    new_sent = ''

    for index in range (0,30):
        new_sent = " "
        message = stockTwits['messages'][index]['body']
        username = stockTwits['messages'][index]['user']['username']
        sentiment = str(stockTwits['messages'][index]['entities']['sentiment'])

        if(sentiment == "{'basic': 'Bullish'}"):
            new_sent = 'Bullish'

        if(sentiment == "{'basic': 'Bearish'}"):
            new_sent = 'Bearish'

        new_message= parser.unescape(message) #convert the message to get rid of unicode chartacters

        stockTwitsData = {
            'message' : new_message,
            'username' : username,
            'sentiment' : new_sent,
        }

        stockTwits_data.append(stockTwitsData)

    return render_template('test.html', stockTwits_data=stockTwits_data)
