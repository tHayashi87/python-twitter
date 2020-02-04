
# twitter ツイート
# ---------------------------

# twi 認証-----------------------------------
import twi_config
from requests_oauthlib import OAuth1Session

ck = twi_config.API_key
cs = twi_config.API_secret_key
at = twi_config.Access_token
ats = twi_config.Access_token_secret
twitter = OAuth1Session(ck, cs, at, ats)
# -------------------------------------------

url = "https://api.twitter.com/1.1/statuses/update.json"

print("つぶやく内容を入力してください")
print("入力後はエンター")
tweet = input(">> ")
print("-----------------------------------")

prm = {"status": tweet}
req = twitter.post(url, params=prm)

if req.status_code == 200:
    print("ツイートが送信されました")
else:
    print("ERROR: %d" % req.status_code)
