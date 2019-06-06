#!/usr/bin/python3
#-*- coding:utf-8 -*-
# Date: 19-3-20 上午11:46
# Author:张印
# Desc：
import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'starpro.settings'
django.setup()
from django.views.decorators.csrf import csrf_exempt
import sys
import codecs
import imgkit
from django.conf import settings
from django.http import HttpResponse
import json
from django.core.management.base import BaseCommand
from starpro.custom_settings import *
from fqd.views.fqd_1688_new import save_sizep_image
reload(sys)
import time
from pyvirtualdisplay import Display
from starpro.settings import *

UNIT_SWITCH_DICT={
    'cm_in':1/2.54,
    'in_cm':2.54,
}

class Command(BaseCommand):
    def handle(self, *args, **options):
        1

@csrf_exempt
def deal_size_table(request):
    display = Display(visible=0, size=(800, 1200))
    display.start()  # 打开虚拟窗口
    try:
        result=True
        message='保存成功'
        user = str(request.user.id)
        file_base = str(settings.MEDIA_ROOT + 'datafile' + "/deal_size/")
        rows = int(request.POST.get("rows"))
        cols = int(request.POST.get("cols"))
        source = request.POST.get("source")
        target = request.POST.get("target")
        html_file ,max_width= excel_html(request, file_base,user,rows,cols,source,target)
        sample_item_id = request.POST.get('sample_item_id')
        suffix = request.POST.get('suffix')
        time_num,img_obj=html_image(html_file, file_base,max_width)
        size_pic = push_img_to_oss(time_num)
        os.remove(img_obj)#删除刚存的图片
        save_sizep_image(size_pic, sample_item_id, suffix)
    except Exception,e:
        result=False
        message = str(e)
    display.stop()
    return HttpResponse(json.dumps({'result': result,'message':message}), content_type='application/json')

def list_items(rows,cols,value_list):
    """
    查询数据
    :param params:
    :return:
    """

    new_value_list = []
    for i in range(rows):
        temp_list = []
        for j in range(cols):
            index = i*cols+j
            temp_list.append(value_list[index])
        new_value_list.append(temp_list)
    total = len(new_value_list)
    return total,new_value_list

def push_img_to_oss(time_num):
    import oss2
    access_key_id=OSS_ACCESS_KEY_ID
    access_key_secret=OSS_ACCESS_KEY_SECRET
    auth=oss2.Auth(access_key_id,access_key_secret)
    bucket = oss2.Bucket(auth,OSS_BUCKET_ENDPOINT_STARMERX[len(OSS_BUCKET_NAME_STARMERX)+1+8:],OSS_BUCKET_NAME_STARMERX)
    result = bucket.put_object_from_file(str(time_num) + ".png", str(MEDIA_ROOT + 'datafile/deal_size/'+str(time_num) + ".png"))
    return str(result.resp.response.url)


def excel_html(request, html_path,user,rows,cols,source,target):
    value_list = request.POST.getlist("value_list[]")
    total,new_value_list=list_items(rows,cols,value_list)
    html_file = html_path + user+".html"
    with codecs.open(html_file, 'w', 'utf-8') as html:
        #用传回的数据 拼接字符串写到html中
        th_strs = ''''''
        td_strs = ''''''
        max_width = ((len(sorted(value_list, key=lambda x: len(x))[-1]) + 3) * 2 * 5) * cols
        for i,th in enumerate(new_value_list):
            if i==0:
                for x in th:
                    th_strs+='''<th>'''+x+'''</th>'''
                th_strs='''<tr>'''+th_strs+'''</tr>'''
            else:
                if i%2!=0:
                    color = '''bgcolor="#d3d3d3"'''
                else:
                    color = '''bgcolor="#FFFFFF"'''
                temp_str = ''''''
                for x in th:
                    x=deal_size_unit(x,source,target)
                    temp_str+='''<td '''+color+'''''''>'''+x+'''</td>'''
                td_strs+='''<tr>'''+temp_str+'''</tr>'''

        html_str = '''<!DOCTYPE html><html>
                    <style>
                    * {padding: 0;margin: 0;font-family: SimSun;}
                    td {text-align: center;vertical-align: middle;height:20px;}
                    th {text-align: center;vertical-align: middle;height:20px;}
                    table{border-collapse: collapse;border-spacing: 0;table-layout: fixed;}
                    .tab{ border-radius: 20px;margin: auto;position: absolute;top: 0;left: 0;right: 0;bottom: 0;}
                    </style>
                    <table class = "tab" border="1" width=" '''+str(max_width)+'''' ''  ";cellpadding="0";cellspacing="0" ;bordercolor="#030303" >  
                      <thead>
                      <meta charset='UTF-8'>
                    '''+th_strs+'''
                      </thead>
                      <tbody>
                    '''+td_strs+'''
                      </tbody>
                    </table>'''
        html.write(html_str)
    return html_file,max_width
def html_image(html_file, image_path,max_width):
    options = {
        'width': max_width+100,
        'height': max_width+100,
        'encoding': 'utf-8',
    }
    time_num=str(time.time())
    img_obj = ''.join([image_path,time_num,".png"])
    with open(html_file) as html_file:
        imgkit.from_file(html_file, img_obj, options=options)
    return time_num,img_obj
def deal_size_unit(x,source,target):
    type = False
    if isinstance(x, int):
        type = 'int'
        x = int(x)
    elif str(x).isdigit():
        type = 'sint'
        x = float(x)
    elif isinstance(x, float):
        type = 'float'
    else:
        try:
            x = float(x)
            type = 'sfloat'
        except Exception:
            pass
    try:
        if type and source!=target:
            return '%.f'%float(x) +source + '/' + '%.1f'%(x*UNIT_SWITCH_DICT[source+'_'+target]) + target
        elif type and source==target :
            return '%.f'%float(x)+source
        else:
            return x
    except Exception,e:
        return e