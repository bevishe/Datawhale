# _*_ coding:utf-8 _*_

class movie(object):
    '''
    一个电影对象，
    '''
    # 电影名字，剧照url、电影url，导演，主演，类别，关键词，评分（10分制），评论人数
    def __init__(self,title,img_url,movie_url,director_name,actor_name,category,key_word,grade,comments):
        __title = title
        __image_url = img_url
        __movie_url = movie_url
        __director_name = director_name
        __actor_name = actor_name
        __category = category
        __key_word = key_word
        __grade = grade
        __comments = comments

