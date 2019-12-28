#-*- coding:utf-8 -*-
from lxml import etree
import requests
from threading import Thread ,enumerate
import os
from time import sleep ,time
import execjs
import urllib
import json

def encodeURI(URIstring ,encoding='gbk'):
    encode_text = URIstring.encode(encoding)
    encode_text = urllib.pathname2url(encode_text)
    return encode_text

def decodeURI(URIstring ,encoding='gbk'):
    encode_text = urllib.pathname2url(URIstring ,encoding)
    return encode_text

def search_novel(name="万古杀帝"):
    url = "https://www.bookbao8.com/Search/q_"
    name_encode = execjs.eval("encodeURIComponent(escape('{name}'))")
    seach_link = url + name_encode
    return seach_link

def url_encode(unicode_text="万古杀帝"):
    data = {
        'data': unicode_text,
        'type': 'urlencode',
        'arg': 's=gb2312_j=0_t=0'
    }
    r = requests.post('http://web.chacuo.net/charseturlencode' ,data=data)
    encode_text = ''
    if r.status_code == requests.codes.ok:
        json_text = json.loads(r.text)
        encode_text = json_text['data'][0]
    return encode_text
def getIndexUrl(name='万古杀帝'):
    r = requests.get(search_novel(name) ,headers=headers)
    if r.status_code == requests.codes.ok:
        r.encoding = r.apparent_encoding
        page_source = etree.HTML(r.text)
        href = page_source.xpath('/html/body/div[6]/div[1]/div[3]/ul/li/div[2]/span/a/@href')
        href = map(lambda x :'https://www.bookbao8.com{x}' ,href)
        name = page_source.xpath('/html/body/div[6]/div[1]/div[3]/ul/li/div[2]/span/a/span/text()')
        novels = list(zip(name ,href))
        return novels
    else:
        return []


headers ={
    # ':authority':'www.bookbao8.com',
    # ':method': 'GET',
    # ':path': '/book/201506/04/id_XNDMyMjA1.html',
    # ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'Hm_lvt_79d6c18dfed73a9524dc37b056df45ec=1577182135; Hm_lpvt_79d6c18dfed73a9524dc37b056df45ec=1577182135; Hm_lvt_9e424f40a62d01a6b9036c7d25ce9a05=1577182142; trustedsite_visit=1; bk_ad=2; __cm_warden_uid=840a745a752905060cd14982b4bbc922coo; __cm_warden_upi=MTE5LjQuMjI4LjE1Nw%3D%3D; Hm_lpvt_9e424f40a62d01a6b9036c7d25ce9a05=1577185720',
    'referer': 'https://www.bookbao8.com/book/201506/04/id_XNDMyMjA1.html',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

def thread_it(func ,*args):
    t = Thread(target=func ,args=args)
    t.setDaemon(True)
    t.start()

def getAll(url = "https://www.bookbao8.com/book/201506/04/id_XNDMyMjA1.html"):
    r = requests.get(url ,headers=headers)
    # print(r.text)
    if r.status_code == 200:
        r.encoding = r.apparent_encoding
        ret = r.text
        page_source = etree.HTML(ret)
        name = page_source.xpath('//*[@id="info"]/h1/text()')
        author = page_source.xpath('//*[@id="info"]/p[1]/a/text()')
        novel_type = page_source.xpath('//*[@id="info"]/p[2]/a/text()')
        title = page_source.xpath('/html/body/div[7]/ul/li/a/text()')
        link = page_source.xpath('/html/body/div[7]/ul/li/a/@href')
        link = map(lambda x: 'https://www.bookbao8.com ' +x, link)  # 向列表中每个元素都加入前缀
        novel_list = list(zip(title ,link))  # 将两个列表用zip打包成新的zip对象并转为列表对象
        if len(novel_list) > 0:
            return name[0], author[0], novel_type[0], novel_list
        else:
            return None ,None ,None ,None

def getOne(link=('第0001章 绝地中走出的少年', 'https://www.bookbao8.com/views/201506/04/id_XNDMyMjA1_1.html')):
    r = requests.get(link[1], headers=headers)
    if r.status_code == 200:
        r.encoding = r.apparent_encoding
        ret = r.text
        page_source = etree.HTML(ret)
        node_title = link[0]
        node_content = page_source.xpath('//*[@id="contents"]/text()')
        node_content = "".join(node_content).replace("\n \xa0 \xa0" ,"")
        if len(node_title) > 0:
            return node_title, node_content
        else:
            return None, None
def writeOne(title ,content):
    txt = "\t\t " +title +"\n " +content +"\n\n"
    return txt
def runApp(novel_list ,name ,t1 ,cwd=''):
    article_num = len(novel_list)
    xc_num = article_num/20 +1
    print "待开启线程数量为{xc_num}"

    def inter(link ,f ,i):
        try:
            title, content = getOne(link)
            txt = writeOne(title, content)
            f.write(txt)
            print "\r线程{i}正在写入 {title}"
        except Exception as e:
            print("\n爬得太快被拒绝连接，等1s递归继续")
            sleep(1)
            inter(link ,f ,i)

    def inner(name ,i ,begin ,end ,cwd):
        f = open("{cwd}downloads/{name}/{i}.txt", mode='w+', encoding='utf-8')
        for link in novel_list[begin:end]:
            inter(link, f ,i)
            if link == novel_list[end - 1]:
                print "\n线程{i}执行完毕"
                print "\n剩余线程数量{len(enumerate())}"
                base_xc = 2 if not cwd else 4
                if len(enumerate()) <= base_xc:
                    print(enumerate())
                    print("\n全本下载完毕")
                    t2 = time()
                    print "\n本次下载小说总共耗时{round(t2 - t1)}s"
                    hebing("{cwd}downloads/{name}")

        f.close()

    for i in range(1 ,xc_num +1):
        begin = 20 *( i -1)
        end = 20 *i if i != xc_num else article_num
        if i == xc_num:
            print "\n全部线程开启完毕"
        thread_it(inner ,name ,i ,begin ,end ,cwd)
        sleep(0.5)

def paixuRule(elem):
    return int(elem.split(".")[0])

def hebing(path):
    dirs = os.listdir(path)
    dirs.sort(key=paixuRule, reverse=False)
    f = open(path +".txt" ,mode='w+' ,encoding='utf-8')
    for file in dirs:
        with open(path +"/ " +file ,mode="r" ,encoding="utf-8") as f1:
            f.write(f1.read())
    f.close()
    print("小说合并完成")
def main(novel_name = "万古杀帝"):
    t1 = time()
    novel_url = getIndexUrl(novel_name)
    if len(novel_url) >= 0:
        url = novel_url[0][1]
    else:
        url = "https://www.bookbao8.com/book/201506/04/id_XNDMyMjA1.html"
    name, _, _, novel_list = getAll(url)
    print(name)
    if not os.path.exists("downloads/" + name):
        os.mkdir("downloads/" + name)
    runApp(novel_list, name, t1)


if __name__ == '__main__':
    main('万古杀帝')
    while True:
        pass