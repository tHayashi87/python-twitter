# twitter ツイート
# ---------------------------
import schedule
import requests
import time

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

def tenki_tweet():

    url01 = "https://api.twitter.com/1.1/statuses/update.json"

    print("つぶやく内容を入力してください")
    print("入力後はエンター")
    tweet = print("test")
    print("-----------------------------------")

    prm = {"status": tweet}
    req = twitter.post(url01, params=prm)

    if req.status_code == 200:
        print("ツイートが送信されました")
    else:
        print("ERROR: %d" % req.status_code)

    # お天気APIと大阪の地域コード
    url02 = "http://weather.livedoor.com/forecast/webservice/json/v1"
    osaka = {"city": "270000"}
    # 上のurlと地域でデータ取得
    tenki_data = requests.get(url02, params=osaka).json()

    # 今日
    today = tenki_data["forecasts"][0]
    # タイトル表示
    print(tenki_data["title"])
    # 日付表示
    print("日付：" + today["date"])
    # 天気表示
    print("天気：" + today["telop"])
    # 最高気温
    print("最高気温" + today["temperature"]["max"]["celsius"])


# 上の関数を毎日７時に実行
schedule.every().day.at("07:00").do(tenki_tweet)

# 上記実行文を無限ループ
while True:
    schedule.run_pending()
    time.sleep(1)
