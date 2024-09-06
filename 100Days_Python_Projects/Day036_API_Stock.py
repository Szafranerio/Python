import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

STOCK_NAME = input('What is your choice: ')
COMPANY_NAME = input('What is the name of company: ')
STOCK_ENDPOINT = os.getenv('STOCK_ENDPOINT')
NEWS_ENDPOINT = os.getenv('NEWS_ENDPOINT')

TWILIO_SID = os.getenv('TWILIO_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
STOCK_API_KEY = os.getenv('STOCK_API_KEY')
NEWS_API = os.getenv('NEWS_API')

# CLosing price
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY
}
# Yesterday clsoing price

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_data_closing_data = yesterday_data['4. close']
print(yesterday_data_closing_data)

# Day before yesterday

day_before_closing_price = data_list[1]['4. close']
print(day_before_closing_price)

# Positive difference

difference = abs(float(yesterday_data_closing_data) -
                 float(day_before_closing_price))
print(difference)

# Percentage difference

diff_percentage = (difference / float(yesterday_data_closing_data)) * 100
print(diff_percentage)

# If hihger than 5 print get news
if diff_percentage > 4:
    news_params = {
        'apiKey': NEWS_API,
        'qInTitle': COMPANY_NAME
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']
    print(articles)


# Python Slice that cointes first three articles
first_three = articles[:3]
print(first_three)

formatted_article_list = [
    f"Headline: {article['title']}. \nBrief: {article['description']}" for article in first_three]

# Send those articles
client = Client(TWILIO_SID, AUTH_TOKEN)

for article in formatted_article_list:
    message = client.messages.create(
        body=article,
        from_='+14158860884',
        to='+4550275452'
    )