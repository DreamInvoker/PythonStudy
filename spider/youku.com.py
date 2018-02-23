import requests
import os

url="http://upload.qianhuaweb.com/2015/0814/1439516288181.jpg"
root="D://root//"
path = root+url.split("/")[-1]

try:
    if not os.path.exists(root):
        os.makedirs(root)
    if not os.path.exists(path):
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        with open(path,"wb") as f:
            f.write(r.content)
            f.close()
            print("爬取成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
