import subprocess
from functools import partial
subprocess.Popen=partial(subprocess.Popen, encoding='utf-8')
import execjs
import requests
import json

url = ""
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.qimingpian.com',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
data = {
    'page': '1',
    'num': '20',
    'sys': 'vip',
    'keywords': '',
    'unionid': '',
}
url = 'https://vipapi.qimingpian.cn/search/recommendedItemList'
response = requests.post(url, headers=headers,data=data).json()
encrypt_data = response["encrypt_data"]
with open("./project/error.js","r+",encoding="utf-8") as file:
    raw_js = file.read()

function_decode = execjs.compile(raw_js)
print(encrypt_data)
print(function_decode.call("s",encrypt_data))
