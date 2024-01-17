import execjs

import requests
import json

url = ""

with open("./test1.js","r+",encoding="utf-8") as file:
    raw_js = file.read()

function_decode = execjs.compile(raw_js)

print(function_decode.call("s",1))
