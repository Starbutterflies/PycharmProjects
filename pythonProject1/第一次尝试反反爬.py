import requests

cookies = {
    'fqYLVbsaziaNS': '60wSocIK6Fk4vunjtcjQD4END0WeWPyAFZcvkP8krKjMbA40dO1_bnsgv4V3HvojxxGR1reqhD4fKAz0flrn3iya',
    'UM_distinctid': '18c6b9f541e13d-0dfa577a755f2b-26001951-d1454-18c6b9f541f14f5',
    'CNZZDATA1264458526': '1135601853-1702612653-http%253A%252F%252Fwww.czce.com.cn%252F%7C1702612653',
    'fqYLVbsaziaNT': '0psU2tVsUeYxrmhjr1NebvXO5dJWZRXATFmmsWdYypjNcrcguw1lnvAgtcJ0tSgQFBT.hJpHIkivlcxzoiLCNUEKCjpJiwdVSXnc14135GbR3DhT4BzQlw_YD6RUOItSZAhyFOpA5rS310GckxPvQB47C3qxrQMKttHbuOs1_j6YJhnKXDXXm6Q7mCj4KMbcOhRuqxbMKnohmKcwhnI2iHgA7g2KCMaqjwGNHkBHbxgq3IWU0D7nMbWG5ZO1NYMCcpS98QgvG1vmDePAjwZQ5R40kBjmv8Vxq9Xq4YyxaPBMjas77kOJoh.5TJ35mA4Hm7TEiftegh0yorn9cVrkfyKAEZi5ISzky4AO1tD3uv8W',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    # 'Cookie': 'fqYLVbsaziaNS=60wSocIK6Fk4vunjtcjQD4END0WeWPyAFZcvkP8krKjMbA40dO1_bnsgv4V3HvojxxGR1reqhD4fKAz0flrn3iya; UM_distinctid=18c6b9f541e13d-0dfa577a755f2b-26001951-d1454-18c6b9f541f14f5; CNZZDATA1264458526=1135601853-1702612653-http%253A%252F%252Fwww.czce.com.cn%252F%7C1702612653; fqYLVbsaziaNT=0psU2tVsUeYxrmhjr1NebvXO5dJWZRXATFmmsWdYypjNcrcguw1lnvAgtcJ0tSgQFBT.hJpHIkivlcxzoiLCNUEKCjpJiwdVSXnc14135GbR3DhT4BzQlw_YD6RUOItSZAhyFOpA5rS310GckxPvQB47C3qxrQMKttHbuOs1_j6YJhnKXDXXm6Q7mCj4KMbcOhRuqxbMKnohmKcwhnI2iHgA7g2KCMaqjwGNHkBHbxgq3IWU0D7nMbWG5ZO1NYMCcpS98QgvG1vmDePAjwZQ5R40kBjmv8Vxq9Xq4YyxaPBMjas77kOJoh.5TJ35mA4Hm7TEiftegh0yorn9cVrkfyKAEZi5ISzky4AO1tD3uv8W',
    'Pragma': 'no-cache',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://www.czce.com.cn/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://www.czce.com.cn/B5sapuOTxHIB/nbD1XNvU80r2.f3df09d.js',
    cookies=cookies,
    headers=headers,
    verify=False,
)
with open("1234.js","wb+") as file:
    file.write(response.content)
