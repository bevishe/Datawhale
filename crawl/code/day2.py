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
    pattern = re.compile('.*?global-nav-items.*?ol class="grid_view".*?<li>.*?<div.*?item.*?<div.*?pic<a href=(.*?)><img.*?alt=.*?src(.*?)class><//a><//div>.*?info.*?hd.*?title">(.*?)<//span>.*?class="bd".*?<p class>(.*?)<//p>.*?<//li>',re.S)
    items = re.findall(pattern,html)
    print(len(items))
    for item in items:
        print(item[0],item[1],item[2],item[3])
    print('hello')

if __name__ == '__main__':
    html = get_one_page("https://movie.douban.com/top250").content.decode('utf-8')
    print(html)
    parse_one_page(html)
    print("main")

