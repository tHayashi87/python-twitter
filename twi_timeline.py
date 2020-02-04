
# twitter timeline取得
# ---------------------------

import json

# twi 認証-----------------------------------
import twi_config
from requests_oauthlib import OAuth1Session

ck = twi_config.API_key
cs = twi_config.API_secret_key
at = twi_config.Access_token
ats = twi_config.Access_token_secret
twitter = OAuth1Session(ck, cs, at, ats)
# -------------------------------------------

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

prm = {"count": 5}
req = twitter.get(url, params=prm)

if req.status_code == 200:
    tl = json.loads(req.text)
    for tweet in tl:
        print(tweet["user"]["name"]+"：\n"+tweet["text"])
        print("(" + tweet["created_at"] + ")")
        print("---------------------------------------")
else:
    print("ERROR: %d" % req.status_code)
