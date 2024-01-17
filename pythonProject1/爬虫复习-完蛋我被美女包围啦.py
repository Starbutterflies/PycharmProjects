import requests
from bs4 import BeautifulSoup
import os
import random
headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-GB;q=0.6",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
        "cookie":"FZ_STROAGE.vcg.com=eyJTRUVTSU9OSUQiOiI5Yjc0NWY4ZGFhMTk3Y2U0IiwiU0VFU0lPTkRBVEUiOjE3MDIwMzUwNDE2Mzd9; ARK_ID=undefined; acw_tc=276077c517021139214416863e0d6ffb298d03c3404c759827aec03405615f; clientIp=111.165.40.231; uuid=7b078bf8-344b-4a38-a89a-a036b49d0206; Hm_lvt_5fd2e010217c332a79f6f3c527df12e9=1702034592,1702113923; fingerprint=a049fa70e3e686e58b655f81587ccc34; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22879de613447c9ad19685e928606083909%22%2C%22first_id%22%3A%2218c492accfbe85-0d9d1c95bcb773-4c657b58-857172-18c492accfd1331%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218c492accfbe85-0d9d1c95bcb773-4c657b58-857172-18c492accfd1331%22%7D; api_token=ST-739-be09c3cb94fb0b3ca6e1bdf1f31165527; abBoss3=1.0; name=18835237517; Hm_lpvt_5fd2e010217c332a79f6f3c527df12e9=1702113968; _fp_=eyJpcCI6IjExMS4xNjUuNDAuMjMxIiwiZnAiOiJhMDQ5ZmE3MGUzZTY4NmU1OGI2NTVmODE1ODdjY2MzNCIsImhzIjoiJDJhJDA4JEMvYnRrT0NyUElDMU8uVU80UDAucS5jYVBhcHE2eHlhL3BSdHRGT1JKVHBXOTlsbVNsYmh1In0%3D; ssxmod_itna=QqmxcDyDgD0i34iq0LYYIEPgj9h40KrPpjqIQD/jQID3q0=GFDf47fogYDCioCQ075+Wx5mrwpWY3jR4hxEDZdPwfTYQx0aDbqFhQGIDYYDtxBYDQxAYDGDDPDoxqD1UD0KDF8Ny/ZyDYPDEnK=DGeDec9ODY5DhxDCDGKHDQKDux5qDG5qzR07YQ9te+YHQSbpn=D+1nKD91oDsOGjQnKmuFdqMhYL1Y73vx0kqq0Oyg4s0WoDUDHsBoYFrm4xWButT703q72t3exqqD4PeCtYmke476wPzf0MeYKKAWNDiZtK1mhDD; ssxmod_itna2=QqmxcDyDgD0i34iq0LYYIEPgj9h40KrPpjqKG9iyDBqD544Ga+1E1rK+76mx8EvPqFBowhQdMtzjTrGRC6dRXOriWlBDF5sfGDFmsH3uGuz8M1jQyz3DXLvXO=voHIbwyy/MjufIpx=fmgfBSui89MEXim2ln+6DxWjlCC2oxW0wGwNZieeVbQ=rsW2qMnrc9TaePloHvuR9F=2YX3RIin43wo0mWCILzRvxGRWZKUB1K/NUI2PGpCB/+eRxXZv+xpL+6/bUpng0uFXYElkRNX5lYU9xNsKBrS7dwN8gayZ9uVl+gV/Ag=MotxfXzlN2p3Z=0tg6qbNY3tyD4k7Dk7xKY48=DWDG2/G572DShdKG=K0D74xGKKom4S9PUqqGTNFGx4We3K4Dad1hPtEaAhx3T5GRN2o4m2dPgriGdUo3TSNVRYonTqnDbfdCT3onq4ePpxYRgtf34/SD4dKcbHsf44uQG05eoo=0kycC7GdD08DiQKYD"
}
base_url = "https://www.vcg.com/creative-image/meinv/"
def image_geter(url):
        """
        :param url: pageurl
        :return: none, but get all the pic in the page
        """
        html = requests.get(url,headers=headers)
        soup = BeautifulSoup(html.text,"lxml") # 拿到HTML网页
        match_list = soup.find_all(class_="galleryItem") # 寻找到url
        for tags in match_list:
                try:
                        src = tags.img.attrs["data-src"]
                        url = "https:" + src
                        name = tags.a.attrs["title"].rstrip("图片")
                        image_data = requests.get(url,headers=headers)
                        with open(rf'D:\桌面\爬虫复习 美女图片\{name+str(random.randint(1,10000000000))}.jpg',"wb+") as file:
                                file.write(image_data.content)
                except Exception as e:
                        print(e)
        return soup
# 然后实现翻页功能
def new_url_getter(soup,i):
        newurl = "https://www.vcg.com/creative-image/meinv/?page=" + f"{i}"
        return newurl
i = 1
while True:
        i += 1
        soup = image_geter(base_url)
        base_url = new_url_getter(soup,i)
        print(base_url)

