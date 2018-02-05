import urllib.request
from lxml import etree
import re

url='https://www.qiushibaike.com/'
header={
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}
req=urllib.request.Request(url,headers=header)
html=urllib.request.urlopen(req).read()
tree=etree.HTML(html)
result=tree.xpath('//div[@class="author clearfix"]')
duanzi=''
data_all=''
for div in result:
    # 作者姓名
    author=div.xpath('.//h2/text()')[0].strip()
    data_all+=('作者：'+author+'\n')
    print('作者：'+author)
    #  判断是否为匿名用户
    age=div.xpath('.//div[@class="articleGender manIcon" or "articleGender womenIcon"]/text()')
    if len(age)>0:#如果不是匿名用户
        print('年龄：' + age[0])
        data_all += ('年龄：' + age[0]+'\n')
        gender=div.xpath('.//div/@class')[0]
        if gender=='articleGender manIcon':
            gender='男'
            data_all+=('性别：'+gender+'\n')
        else:
            gender='女'
            print('性别:'+gender)
            data_all += ('性别：' + gender+'\n')
    else:
        print('年龄：' + '不详')
        data_all += ('年龄：' + '不详'+ '\n')
        print('性别:' + '不详')
        data_all += ('性别：' + '不详' + '\n')
    # 好笑数
    fun_num=div.xpath('..//span[@class="stats-vote"]/i[@class="number"]/text()')
    if len(fun_num)>0:
        print('好笑数:' + fun_num[0])
        data_all += ('好笑数:' + fun_num[0]+'\n')
    else:
        print('好笑数:0')
        data_all += ('好笑数:0'+'\n')
    # 评论数
    comment_num = div.xpath('..//a/i[@class="number"]/text()')
    if len(comment_num)>0:
        print('评论数:' + comment_num[0])
        data_all += ('评论数:' + comment_num[0]+'\n')
    else:
        print('评论数:0')
        data_all += ('评论数:0'+'\n')
    #段子
    content=div.xpath('..//div[@class="content"]/span/text()')
    for text in content:
        duanzi+=text.strip()
    print('段子：'+duanzi)#得到的段子
    data_all+=('段子：'+duanzi+'\n\n')
    duanzi=''#为了下一次循环，做初始化
    print("============")

with open('qsbk.txt','w',encoding='utf-8') as f:
    f.write(data_all)
