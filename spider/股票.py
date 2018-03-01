import requests
import re
from bs4 import BeautifulSoup
import traceback

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getStockList(lst,stockURL):
    try:
        r = requests.get(stockURL, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    return ""


def getStockInfo(lst,stockURL,fpath):
    print("")

def main():
    stock_list_url = ""
    stoc_info_url ="https://gupiao.baidu.com/stock/"
    output_file="D://baidu.txt"
    slist=[]

getHTMLText()