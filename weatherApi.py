import schedule
import requests
import time

def tenki():
    # お天気APIと大阪の地域コード
    url = "http://weather.livedoor.com/forecast/webservice/json/v1"
    osaka = {"city": "270000"}
    # 上のurlと地域でデータ取得
    tenki_data = requests.get(url, params=osaka).json()

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
schedule.every().day.at("07:00").do(tenki)

# 上記実行文を無限ループ
while True:
    schedule.run_pending()
    time.sleep(1)

