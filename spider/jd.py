import requests
url = r"https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BAmate10&enc=utf-8&wq=%E5%8D%8E%E4%B8%BAmate10&pvid=3474b9154b36497183b5203d17d5626e"

try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
except:
    print('爬取失败')