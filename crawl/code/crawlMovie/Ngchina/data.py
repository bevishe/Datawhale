# _*_ coding:utf-8 _*_
import requests
from lxml import etree
import oneImg

# 对url发起请求同时返回页面html
from requests.packages.urllib3.exceptions import ResponseError


def get_html(url):
    headers = {}
    try:
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response
        else:
            print('请求页面返回状态码错误')
    except ResponseError:
        print(ResponseError)


# 获取一级页面中所有的href，一页获取完之后返回第二页的
def get_href(html):
    href_list = []
    html = etree.HTML(html)
    href = html.xpath('/html/body/div/div/div/ul/li/div/h5/a/@href')
    for i in href:
        print(i.strip())
        href_list.append(i.strip())
    return href_list

# 解析二级页面中的每个图片的具体信息，并打印出来
def parse_img(html):
    html = etree.HTML(html)
    # title,time,img_url,content,cameraman
    title = html.xpath('/html/body/div[4]/div[1]/div/div[2]/ul/li/p//text()')
    time = html.xpath('/html/body/div[4]/div[2]/div[1]/div[1]/div/div[1]/text()')
    img_url = html.xpath('/html/body/div[4]/div[1]/div/div[1]/ul/li/a/img/@src')
    content = html.xpath('/html/body/div[4]/div[2]/div[1]/div[2]/div[1]/text()')
    cameraman = html.xpath('/html/body/div[4]/div[2]/div[1]/div[2]/div[3]/text()')
    img = oneImg.img_info(title,time,img_url,content,cameraman)
    return img

# 爬取主函数
def crawl(url,start_url):
    # 获取到所有的href列表
    one_html = get_html(start_url).content.decode('utf-8')
    href_list = get_href(one_html)
    for _ in href_list:
        print(_)
        two_html = get_html(url+_).content.decode('utf-8')
        img = parse_img(two_html)
        print(img)


if __name__ == '__main__':
    crawl(url = 'http://www.ngchina.com.cn',start_url = 'http://www.ngchina.com.cn/photography/photo_of_the_day/')