# _*_ coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import RequestError
from lxml import etree

from movie import movie


def get_one_html(url):
    try:
        response = requests.get(url = url)
        if response.status_code == 200:
            return response
        else:
            print("接收页面失败")
    except RequestError:
        print(RequestError)

def get_ol_li_tag(tag):
    return tag.has_attr('class')

def parse_one_html(html):
    movies_list = []
    soup = BeautifulSoup(html,'lxml')
    ol_tag = soup.find_all('li')
    for _ in ol_tag:
        li_tag = _.find_all('div')
        print(li_tag)

def get_one_html_lxml(html):
    resutl_list = []
    html = etree.HTML(html)
    # title,img_url,movie_url,director_name,actor_name,category,time,country,key_word,grade,comments,movie_url
    # big = html.xpath('//*[@id="content"]/div/div[1]/ol/li')
    # print(big[0].xpath('div/div[2]/div[1]/a/span[1]/text()'))
    # print(big[0].xpath('div/div[1]/a/img/@src'))

    title = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')
    img_url = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[1]/a/img/@src')
    movie_url = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[1]/a/@href')
    comments = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[2]/span/text()')
    print(len(title))
    for i in range(0 ,len(title)):
        resutl_list.append(movie(title[i],img_url[i],movie_url[i],comments[i]))
        print(""+title[i]+img_url[i]+movie_url[i]+comments[i])

    #print(html_xml.xpaht('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]'))


if __name__ == '__main__':
    get_one_html_lxml(get_one_html('https://movie.douban.com/top250').text)