import requests
from bs4 import BeautifulSoup
import os
from threading import Thread
import time


def singlechapter(url, chapter_name, novel_name, i):  # 定义函数下载每一章内容
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    r = requests.get(url, headers=head)
    r.encoding = r.apparent_encoding  # 使编码正常
    soup = BeautifulSoup(r.text, "html.parser")  # 解析
    soup1 = soup.find('div', id='content')
    try:
        soup1.find('p').extract()  # 清除p标签中的广告
    except:
        pass
    f = open('d://novel//'+str(novel_name)+'//'+novel_name +
             str(i)+'.txt', 'a', encoding='utf-8')
    f.write(chapter_name)
    print("\r当前下载章节为:"+chapter_name+'                        ', end="")  # 写入章节名
    f.write('\n')
    f.write(soup1.text)
    f.close()


def singlenovel(url):  # 定义函数找出每一章的url
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    r = requests.get(url, headers=head)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, "html.parser")
    soup1 = soup.find_all('dd')
    list_url = []  # 用于存放每个章节的url
    list_chapter = []  # 用于存放每个章节的名字
    lsit_noveln_name = []  # 用于存放该小说的名字
    soup2 = soup.find_all('div', {'id': 'info'})
    for i in soup2:
        k = i.find('h1')
        lsit_noveln_name.append(k.text)
    print("当前下载小说为:", lsit_noveln_name[0])
    for i in soup1:
        j = i.find_all('a')
        for k in j:
            list_url.append('http://www.xbiquge.la'+k.get('href'))
            list_chapter.append(k.text)

    for i in range(0, len(list_chapter)):
        Thread(target=singlechapter, args=(
            list_url[i], list_chapter[i], lsit_noveln_name[0], i)).start()
        # singlechapter(list_url[i],list_chapter[i],lsit_noveln_name[0])


if __name__ == '__main__':
    url = "http://www.xbiquge.la/xiaoshuodaquan/"
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    r = requests.get(url, headers=head)
    soup = BeautifulSoup(r.text, "html.parser")
    soupli = soup.find_all('li')
    # print(soupli)
    list_url = []  # 用于存放所有小说的url
    list_name = []  # 用于存放所有小说的名字
    dic_name = {}  # 用于把名字和对应的url存放起来
    try:
        os.makedirs('d://novel')  # 建立存储地址
    except:
        pass
    for i in soupli:
        j = i.find_all('a')
        for k in j:
            list_name.append(k.text)
            list_url.append(k.get('href'))
    list_url = list_url[10:]  # 删去无用的错误网址
    list_name = list_name[10:]  # 删去无用的错误名字
    for i in range(0, len(list_name)):
        dic_name[list_name[i]] = list_url[i]
    print('当前收录小说一共'+str(len(list_name))+'本')
    temp = input('输入你想下载的小说:')
    if temp in dic_name:
        print('小说下载地址为D://novel')
        print('此小说url为：' + str(dic_name[temp]))
        try:
            path = 'd://novel//' + str(temp)
            os.makedirs(path)  # 建立小说对应地址
        except:
            pass
        singlenovel(dic_name[temp])
    else:
        print('暂时没有这本小说')
    print('')
    print('操作完成')
