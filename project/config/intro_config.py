# -*- coding:UTF-8 -*-
import os
import ConfigParser
def intro_conf(name):
    curpath = os.path.dirname(__file__)
    ini_path = os.path.join(curpath, name)
    #创建管理对象
    cfg = ConfigParser.ConfigParser()
    #读取配置文件
    cfg.read(ini_path)
    return  cfg