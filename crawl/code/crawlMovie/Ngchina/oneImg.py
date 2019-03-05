# _*_ coding:utf-8 _*_

class img_info(object):
    '''
    title,time,摄影师，img_url，简介
    '''
    def __init__(self,title,time,img_url,content,cameraman):
        self.title = title
        self.time = time
        self.img_url = img_url
        self.content = content
        self.cameraman = cameraman

    def __str__(self) -> str:
        return "title：%s\r\ntime:%s\r\nimg_url:%s\r\ncontent:%s\r\ncameraman:%s"%(self.title,self.time,self.img_url,self.content,self.cameraman)

    __repr__ = __str__


