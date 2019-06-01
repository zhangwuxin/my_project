#!/usr/bin/python3
#-*- coding:utf-8 -*-
# Date: 19-5-27 下午5:37
# Author:张印
# Desc：
import re
def out_re (str,source):
    print re.match(str, source).group()

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
#匹配出163的邮箱地址，且@符号之前有4到20位，例如hello@163.com
out_re("[\w]{4,20}@163\.com$","_Ahello@163.com")
out_re(r".*\bver\b", "ho ver abc")