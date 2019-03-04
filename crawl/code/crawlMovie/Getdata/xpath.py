import requests
from lxml import etree
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

def get_one_html_lxml(html):
    html = etree.HTML(html)
    big = html.xpath('//*[@id="postcontainer"]')
    for _ in big:
        # 获取用户名
        print(_.xpath('div/table/tbody/tr/td[1]/div[2]/a/text()'))
        # 获取发表的内容
        print(_.xpath('div/table/tbody/tr/td[2]/div[2]/div[2]/table/tbody/tr/td/text()'))
    # name = big.xpath('div/table/tbody/tr/td[1]/div[2]/a/text()')
    # content = big.xpath('div/table/tbody/tr/td[2]/div[2]/div[2]/table/tbody/tr/td/text()')
    # for i in range(0,len(big.xpath('div'))):
    #     print(name[i])
    #     print(content[i])


if __name__ == '__main__':
    html = get_one_page('http://www.dxy.cn/bbs/thread/626626#626626').text
    get_one_html_lxml(html)