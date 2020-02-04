
import schedule
import requests
import time
import json

# twi 認証-----------------------------------
# 使用する際は twi_config.py というファイルを作成し、
# 各種APIの認証情報を入力してください

import twi_config
from requests_oauthlib import OAuth1Session

ck = twi_config.API_key
cs = twi_config.API_secret_key
at = twi_config.Access_token
ats = twi_config.Access_token_secret
twitter = OAuth1Session(ck, cs, at, ats)
# -------------------------------------------

def tenki_tomorrow():
    # twitter API
    url01 = "https://api.twitter.com/1.1/statuses/update.json"
    # お天気APIと大阪の地域コード
    url02 = "http://weather.livedoor.com/forecast/webservice/json/v1?city=270000"
    # 上のurlと地域でデータ取得
    tenki_data = requests.get(url02).json()
    # 今日
    tomorrow = tenki_data["forecasts"][1]

    tit = tenki_data["title"]
    td = tomorrow["date"]
    tnk = tomorrow["telop"]
    max_cel = tomorrow["temperature"]["max"]["celsius"]
    min_cel = tomorrow["temperature"]["min"]["celsius"]

    tweet = """
    明日のお天気をお知らせします🤗\n\n 
    {0}\n
    {1}\n
    {2}\n
    最高気温{3}度\n
    最低気温{4}度\n
    以上Pythonからの自動ツイートでした☺️
    """.format(tit, td, tnk, max_cel, min_cel)

    print(tweet)
    prm = {"status": tweet}
    req = twitter.post(url01, params=prm)

    if req.status_code == 200:
        print("ツイートが送信されました")
    else:
        print("ERROR: %d" % req.status_code)


# テスト用
# tenki_tomorrow()


# 上の関数を毎日７時に実行
schedule.every().day.at("19:00").do(tenki_tomorrow)

# 上記実行文を無限ループ
while True:
    schedule.run_pending()
    time.sleep(1)
