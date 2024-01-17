import requests

cookies = {
    'acw_tc': 'ac11000117026217899567686e005dd9e01ff6f8b20c44bffa76b895b8f960',
    '_zcy_log_client_uuid': '5a219be0-9b13-11ee-989d-b9145adbc3ea',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'acw_tc=ac11000117026217899567686e005dd9e01ff6f8b20c44bffa76b895b8f960; _zcy_log_client_uuid=5a219be0-9b13-11ee-989d-b9145adbc3ea',
    'Origin': 'http://www.whggzy.com',
    'Pragma': 'no-cache',
    'Referer': 'http://www.whggzy.com/luban/category?parentId=66007&childrenCode=PoliciesAndRegulations&utm=luban.luban-PC-49434.959-pc-websitegroup-navBar-front.4.447b01a09b1311eeb2ce0d0c3efafe2a',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

data = "{\"pageNo\":1,\"pageSize\":15,\"categoryCode\":\"GovernmentProcurement\",\"_t\":1702626531000}"

response = requests.post('http://www.whggzy.com/portal/category', cookies=cookies, headers=headers, data=data, verify=False)
print(response.text)
# 不存在加密方式，但是请求失败，可以进行打断点的方式进行接口校验