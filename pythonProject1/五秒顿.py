import requests

cookies = {
    'Hm_lvt_9511d505b6dfa0c133ef4f9b744a16da': '1702458040',
    '__root_domain_v': '.youzhicai.com',
    '_qddaz': 'QD.184202458040084',
    '_qdda': '2-1.1',
    '_qddab': '2-o4f26m.lq3jk6yh',
    'Hm_lpvt_9511d505b6dfa0c133ef4f9b744a16da': '1702458235',
}

headers = {
    'authority': 'youzhicai.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'Hm_lvt_9511d505b6dfa0c133ef4f9b744a16da=1702458040; __root_domain_v=.youzhicai.com; _qddaz=QD.184202458040084; _qdda=2-1.1; _qddab=2-o4f26m.lq3jk6yh; Hm_lpvt_9511d505b6dfa0c133ef4f9b744a16da=1702458235',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://youzhicai.com/nd/c93b8018-328a-40f4-950b-3d4bdbac44c1-1.html',
    cookies=cookies,
    headers=headers,
)
print(response.text)