import requests

symbol = 'aapl'
api_key = '6f47289aa7a94bdca343732788f30a72'
news_url = 'https://newsapi.org/v2/everything?q=' + symbol + '&from=2018-08-25&sortBy=publishedAt&apiKey=6f47289aa7a94bdca343732788f30a72'
news = requests.get(news_url).json()
news_data = news['articles'][0]['author']


for indx in range (0,10):
    news_data = news_data + news['articles'][indx]['author'] + '\n'


'''
for indx in range (0,10):
    author = news['articles'][indx]['author']
    news_data = []
    news = {
        'author' : author,
    }
    news_data.append(news)
'''
print(news_data)
