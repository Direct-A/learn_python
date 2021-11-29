"""
AppKey：203894380
AppSecret：AAD4WXmbLCwmCEfyRmaE4AdoJ9XqJivm
AppCode：27fe42ab377a45d0a02caa2cb81c65dd

"""
from __future__ import print_function

import ssl, hmac, base64, hashlib
from datetime import datetime as pydatetime

# py2 py3 compatitve
try:
    from urllib import urlencode
    from urllib2 import Request, urlopen
except ImportError:
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen


# basic var define
host = "https://jisuisbn.market.alicloudapi.com"
path = "/isbn/query"
method = "ANY"
appcode = "27fe42ab377a45d0a02caa2cb81c65dd"
querys = "isbn=9787117206464"
bodys = {}
url = host + path + "?" + querys

# pre-run
bodys[""] = ""
post_data = bodys[""]
request = Request(url, post_data)
request.add_header("Authorization", "APPCODE " + appcode)
request.data = urlencode(bodys).encode("utf-8")
# 根据API的要求，定义相对应的Content-Type
request.add_header("Content-Type", "application/json; charset=UTF-8")
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# run
response = urlopen(request, context=ctx)
content = response.read()

# return data
if content:
    print(content.decode("utf-8"))
