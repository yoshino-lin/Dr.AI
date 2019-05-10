# -&- coding: utf-8 -*-
import json,os
import linecache
import yaml
import time
#截图
import win32gui, win32ui, win32con, win32api
#图片识别
import pytesseract
from PIL import ImageGrab, Image

#读取文件
employees_load = (len(open("employees\skyfire.yml",'r',encoding='utf-8').readlines())) #获取干员信息
maps_load = (len(open("maps\CE-3.yml",'r',encoding='utf-8').readlines())) #地图信息

#地图载入
map_file = "maps\CE-3"
map_height_info = linecache.getline(map_file,3)#获取地图宽度，宽度等于加载的循环次数
map_data = [] #创建地图数据的list
#讲地图数据导入到list当中
for i in range(map_height_info-1):
	map_data.append(map_height_info = linecache.getline(map_file,5+i))

#加载干员
def employee_load(employee,level,reliability,elite_level,proficiency_level) #干员名称，等级，信赖度，精英化等级，潜能突破等级
	employee_file_name= employee + ".yml"
	hp_value = linecache.getline(employee_file_name,5)
