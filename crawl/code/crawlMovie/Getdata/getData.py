# _*_ coding:utf-8 _*_
import requests
import re
import movie

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
    '''返回电影对象的列表'''
    movies = []
    pattern = re.compile('<div class="hd">([\d\D]*?)</li>',re.S)
    # items中的每个电影的所有内容，之后需要对其进行切分
    items = re.findall(pattern,html)
    for i in items:
        # i记录了每一个电影所有的的信息
        # title,img_url,movie_url,director_name,actor_name,category,time,country,key_word,grade,comments
        movie_url = re.findall(re.compile('href="(.*?)"',re.S),i)
        img_url = re.findall(re.compile('src="(.*?)" class="">',re.S),i)
        title = re.findall(re.compile('<span class="title">(.*?)</span>',re.S),i)
        director_name = re.findall(re.compile('<div class="bd">.*?<p class>"导演：(.*?)主演',re.S),i)
        actor_name = re.findall(re.compile('主演：(.*?)"'))

        category = re.findall(re.compile(''))




if __name__ == '__main__':
    html = get_one_page("https://movie.douban.com/top250").content.decode('utf-8')
    parse_one_page(html)


