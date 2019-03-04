import  requests
from lxml import etree
url='http://www.dxy.cn/bbs/thread/626626#626626'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
x= requests.get(url, headers=headers, timeout=3)
x.encoding=x.apparent_encoding
wb_data=x.text
html = etree.HTML(wb_data)
data=[]
new_data=[]
result_txt = html.xpath('//td[@class="postbody"]/text()')#找到所需要的数据
print(result_txt)
result_name=html.xpath('//div[@class="auth"]/a/text()')
print(result_name)
for i in range(0,4):
    data.append(result_name[i]+"###"+result_txt[i])
for i in data:
    x=i.replace("\n","").replace("\t","").replace(" ","")
    new_data.append(x)
print(new_data)
