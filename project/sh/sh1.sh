#!/bin/bash
my_name="zy"
greeting="HELLO,"$my_name" !"
echo $greeting
#获取字符串长度
string="asdfs123"
echo ${#string}
#提取子字符串
echo ${string:1:4}
#查找子字符串
string="sf i fdsw sdf"
echo `expr index "$string" io`
#数组
array_name=(a b c d e f g)
echo ${array_name[2]}
