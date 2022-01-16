import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
ALPHA_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/top-headlines"


def send_articles(change_rate: float):
    news_param = {
        "apiKey": os.getenv("NEWSAPI_KEY"),
        "q": COMPANY_NAME

    }
    news_res = requests.get(url=NEWS_URL, params=news_param)
    news_res.raise_for_status()
    recent_articles = news_res.json()["articles"][:3]
    print(recent_articles)

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    if change_rate >= 0:
        mark = "▲"
    else:
        mark = "▼"

    for article in recent_articles:
        client = Client(account_sid, auth_token)

        title = article["title"]
        brief = article["content"]
        content = f"{STOCK}:{mark}{change_rate}% \nHeadline:{title} \nBrief:{brief}"
        # Optional: Format the SMS message like this:
        """
        TSLA: 🔺2%
        Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
        Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
        or
        "TSLA: 🔻5%
        Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
        Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
        """

        message = client.messages \
            .create(
            body=content,
            from_='+11',
            to='+11'
        )


def check_stock_value():
    # STEP 1: Use https://www.alphavantage.co
    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

    stock_param = {
        "apikey": os.getenv("ALPHA_VANTAGE_APIKEY"),
        "symbol": STOCK,
        "function": "TIME_SERIES_DAILY"
    }

    stock_res = requests.get(url=ALPHA_URL, params=stock_param)
    stock_res.raise_for_status()
    stock_daily_data = stock_res.json()["Time Series (Daily)"]

    key_list = []
    for key in stock_daily_data.keys():
        if len(key_list) > 2:
            continue
        else:
            key_list.append(key)

    yesterday_close_value = float(stock_daily_data[key_list[0]]["4. close"])
    dby_close_value = float(stock_daily_data[key_list[1]]["4. close"])

    change_rate = round((yesterday_close_value - dby_close_value) / dby_close_value * 100, 2)

    if change_rate < -1 or 1 < change_rate:
        send_articles(change_rate)


check_stock_value()
