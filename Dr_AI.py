# -&- coding: utf-8 -*-
import json,os
import linecache
import yaml
#截图
import win32gui, win32ui, win32con, win32api
#图片识别
import pytesseract
from PIL import ImageGrab, Image

#地图载入
map_file = "maps\CE-3.yml"
maps_load = (len(open(map_file,'r',encoding='utf-8').readlines())) #地图信息
map_height_info = linecache.getline(map_file,3)#获取地图宽度，宽度等于加载的循环次数
map_data = [] #创建地图数据的list

#讲地图数据导入到list当中
for i in range(1,int(map_height_info)):
	map_data.append(linecache.getline(map_file,4+i))

#加载干员
employees_data_list = []
def employee_load(employee,level,reliability,elite_level,proficiency_level): #干员名称，等级，信赖度，精英化等级，潜能突破等级
	global employees_data_list #获取干员数据存放列表的操作权限
	employee_file_path = "employees\\"+ employee + ".yml" #干员文件的路径
	#读取干员信息并以字典的形式存入列表当中
	employees_data_list.append(yaml.load(open(employee_file_path, 'r', encoding='utf-8'), Loader=yaml.FullLoader))
	print(employees_data_list)
	
	
employee_load("skyfire",1,1,1,1)
