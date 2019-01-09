# -*- coding:UTF-8 -*-
import ConfigParser
import json
import os
#读取配置文件路径
curpath = os.path.dirname(__file__)
ini_path = os.path.join(curpath, "user.ini")
#创建管理对象
cfg = ConfigParser.ConfigParser()
#读取配置文件
cfg.read(ini_path)
#获取所有的section
sections = cfg.sections()
print sections
user_dict = eval(cfg.get('user','user_dict'))
#删除一个section
cfg.remove_section('test')
print cfg.sections()

