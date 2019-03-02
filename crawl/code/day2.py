# _*_ coding:utf-8 _*_
import requests
import re

from requests.packages.urllib3.exceptions import RequestError

# 获得要爬取的页面
def get_one_page(url):
    try:
        response = requests.get(url = url)
        if response.status_code == 200:
            return response
        else:
            print("接收页面失败")
    except RequestError:
        print(RequestError)

# 对下下来的页面进行解析
def parse_one_page(html):
    pattern = re.compile('<div class="hd">([\d\D]*?)</li>',re.S)
    items = re.findall(pattern,html)
    print(items)
    pattern_in = re.compile('href="(.*?)"',re.S)
    for i in items:
        items_in = re.findall(pattern_in,i)
        print(len(items_in))
        print(items_in[0])
        # print(items_in[1])
        # print(items_in[2])
        # print(items_in[3])
if __name__ == '__main__':
    html = get_one_page("https://movie.douban.com/top250").content.decode('utf-8')
    parse_one_page(html)


