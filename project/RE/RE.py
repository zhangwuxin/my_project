#!/usr/bin/python3
#-*- coding:utf-8 -*-
# Date: 19-5-27 下午5:37
# Author:张印
# Desc：
import re
def out_re (str,source,i=0):
    print re.match(str, source).group(i)

out_re('[0123456789]','2hello pyt2hon')
out_re('[Hh]','Hhello pyt2hon')
out_re('[hH]','hello pyt2hon')
out_re('嫦娥\d号','嫦娥1号')
out_re('嫦娥\d号','嫦娥2号')
out_re('嫦娥\d号','嫦娥3号')
out_re(r"https:\\",'https:\\www.baidu.com')
out_re("[A-Z][a-z]*","MmmadasMdsfsf")
out_re("[a-zA-Z_]+[\w_]*","_nameas2_")
out_re("[1-9]?[0-9]","99")
out_re("[a-zA-Z0-9_]{6}","12a3g45678")
#匹配出163的邮箱地址，且@符号之前有4到20位，例如h"[1-9]?\d","8"ello@163.com
out_re("[\w]{4,20}@163\.com$","_Ahello@163.com")
out_re(r".*\bver\b", "ho ver abc")
out_re(r".*\Bver\B", "222f13hoverabc")
out_re("[AD]?\d","D2")
out_re("[1-9]?\d$","8")
string = ' 123 dqw  3，213df,adsd'
print re.sub(' +', ',', string.strip().replace('，', ',')).split(',')
out_re("[1-9]?\d$|100","90")
out_re("\w{4,20}@(163|qq|sina)\.com",'asdf123@163.com')
out_re("([\w+]*)-(\d+)","22-12345678",2)
out_re(r'<html>\w*</html>','<html>sdf</html>')
out_re(r'<([a-zA-Z]*)>\w*</\1>','<html>asd122312</html>')
out_re(r"<(\w*)><(\w*)>.*</\2></\1>", "<html><h1>www.itcast.cn</h1></html>")
out_re(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.itcast.cn</h1></html>")
#search 一次性匹配
print re.search(r"[阅读次数]*(\d+)",'阅读次数sf为9999dff213').group(1)
#search 全部匹配返回list
print re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
#sub 将匹配的数据进行替换
add = lambda temp:str((int(temp.group())+1))
print re.sub(r"\d+",add,"python = 996")
print filter(None,re.split(r"\W","  info:xiaoZhang,33，sh|andong  "))

html2 = '<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">'
print re.findall(r'https:.+\.jpg',html2)

url = 'http://www.interoem.com/messageinfo.asp?id=35'
print re.match(r'http:.+\/',url).group()
words = 'hello world ha ha'
print re.split(r' ',words)