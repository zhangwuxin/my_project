# -*- coding:UTF-8 -*-
import ConfigParser
import sys
import json
import os
from project.config.intro_config import intro_conf
#读取配置文件路径
class deal_ini(object):
    def __init__(self,type,file_name,section,names):
        self.type = type
        self.file_name = file_name
        self.section = section
        self.names = names

        self.TYPE_DICT ={
            'get_sections':self.get_sections,
            'get_section': self.get_section,
            'read_section_itme': self.read_section_itme,
            # 'change': self.change
        }

    def run(self):
        return self.TYPE_DICT.get(self.type)()

    def get_sections(self):
        try:
            cfg = intro_conf(self.file_name)
            result = cfg.sections()
        except Exception as e:
            result = str(e)
        return result

    def get_section(self):
        try:
            cfg = intro_conf(self.file_name)
            result = cfg.items(self.section)
        except Exception as e:
            result = str(e)
        return result

    def read_section_itme(self):
        try:
            cfg = intro_conf(self.file_name)
            result = cfg.get(self.section, self.names)
        except Exception as e:
            result = e
        return result

    # def change(self):
    #     try:
    #         cfg = intro_conf(self.file_name)
    #         cf.get("base",id)
    #         temp_list = cfg.items(self.section)
    #
    #         cfg.set('user', 'port', '8000')
    #         cfg.write(open(self.file_name), "w")
    #     except Exception,e:
    #         result = str(e)
    #     return result

w = deal_ini(file_name='user.ini',type='read_section_itme',section='user',names='PRODUCT_LIFECYCLE1')
result = w.run()

# curpath = os.path.dirname(__file__)
# ini_path = os.path.join(curpath, "user.ini")
# #创建管理对象
# cfg = ConfigParser.ConfigParser()
# #读取配置文件
# cfg.read("user.ini")
# #获取所有的section
# sections = cfg.sections()
# print sections
# user_dict = eval(cfg.get('user','user_dict'))
# #删除一个section
# cfg.remove_section('test')
# print cfg.sections()
# cfg.set('user','port','8000')
# cfg.write(open(ini_path),"w")
# cfg.add_section('test111')
# cfg.set('test111','title','tettt')
# cfg.write(open('user.ini','w'))
# cfg.set('test111','tesetsetset','123123213123')
# cfg.write(open('user.ini','r+'))
