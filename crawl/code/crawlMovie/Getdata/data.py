# _*_ coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import RequestError

def get_one_html(url):
    try:
        response = requests.get(url = url)
        if response.status_code == 200:
            return response
        else:
            print("接收页面失败")
    except RequestError:
        print(RequestError)
    pass

def get_ol_li_tag(tag):
    return tag.has_attr('class')

def parse_one_html(html):
    movies_list = []
    soup = BeautifulSoup(html,'lxml')
    ol_tag = soup.find_all('li')
    for _ in ol_tag:
        li_tag = _.find_all('div')
        print(li_tag)


if __name__ == '__main__':
    html = get_one_html('https://movie.douban.com/top250').text
    parse_one_html(html)