# 问题不大，工具安装成功了
import pandas as pd
import numpy as np
import time
import requests
from bs4 import BeautifulSoup
import random
import json
from jsonpath import jsonpath
# 生成随机数。这个是干什么的呢？这个是用来爬数据的。
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "Accept":"*/*",
    "Connection":"keep-alive",
    "Cookie":"buvid3=33E4C30B-8E73-2BB5-4D4C-54E05B72C62C22303infoc; b_nut=1700145822; i-wanna-go-back=-1; b_ut=7; _uuid=B6A22F4B-BB24-1184-6CB8-5CC2EC108A3B724394infoc; enable_web_push=DISABLE; home_feed_column=4; buvid4=7555AE8B-97E0-A67C-FD63-6C0EA3F8192B25275-023111614-; CURRENT_FNVAL=4048; DedeUserID=438054412; DedeUserID__ckMd5=97bfdda9268af686; SESSDATA=ef7d1a8e%2C1715697928%2C8314e%2Ab1CjAAecPzLND7wejqpmCAcnVPnTdQQqYVfSmdCZQHLDO-DWkTC_1PtTx6vUoQgXWFtIQSVjJqd0RfZWNQQkdGZzVWQnd5ekN6OEZyZnk0UHFzMjNtUXV5QVdJN2JCazNhWWlKV3pMUWlVdy1KM3NBVnlyMUJLaVJ2ZzJ2VFlib3VkZmlOcTlEcFFnIIEC; bili_jct=409d4666431a3682c5016006a4293d51; header_theme_version=CLOSE; rpdid=|(u)~J|)~J~u0J'u~||uRY||l; hit-dyn-v2=1; buvid_fp_plain=undefined; CURRENT_QUALITY=0; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDI0Njk1NzMsImlhdCI6MTcwMjIxMDMxMywicGx0IjotMX0.W7r3EOvBu0XH1OcF0YZxht6WpzRUzQBKCMmgvtaUVl4; bili_ticket_expires=1702469513; bsource=search_bing; sid=62u3rcju; PVID=4; bp_video_offset_438054412=873513137341464600; b_lsid=3B414EA7_18C56788E6E; fingerprint=50c42bbd80e926f9d6026ef7b3ad741a; buvid_fp=50c42bbd80e926f9d6026ef7b3ad741a; browser_resolution=1123-620",    "Referer":"https://www.bilibili.com/video/BV1yC4y1X7Tt/?spm_id_from=333.337.search-card.all.click&vd_source=4b5f6740f66d8d025d459e96edb72ef1"
,"Accept-Encoding":"gzip, deflate, br",
    "Referer":"https://www.bilibili.com/video/BV1yC4y1X7Tt/?spm_id_from=333.337.search-card.all.click&vd_source=4b5f6740f66d8d025d459e96edb72ef1"
}
# 然后试着来一下
urllist = [f"https://api.bilibili.com/x/v2/reply?type=1&oid=792074350&pn={i}"for i in range(1,20)]
comment_list = []
name_list = []
for url in urllist:
    success = False
    while not success:

        try:
            response = requests.get(url,headers=headers)
            jsondata = json.loads(response.text)
            for data in jsonpath(jsondata, "$.data.replies")[0]:
                comment_list.append(data["content"]["message"])
            for name in jsonpath(jsondata, "$.data.replies")[0]:
                name_list.append(name["member"]["uname"])
            success = True  # 当前 URL 处理成功
            time.sleep(1)

        except Exception as e:
            print(f"处理 URL {url} 时发生错误: {e}, 重试...")
            time.sleep(1)  # 在重试前等待一段时间
print(len(comment_list))
print(len(name_list))
pd.DataFrame(name_list,comment_list).to_csv("D:/桌面/安迪视频评论.csv",encoding="utf8")
