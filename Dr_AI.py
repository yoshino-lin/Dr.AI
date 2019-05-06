# -&- coding: utf-8 -*-
import json,os
import linecache
import yaml

#读取文件
employees_load = (len(open("employees\skyfire.yml",'r',encoding='utf-8').readlines())) #获取干员信息
maps_load = (len(open("maps\CE-3.yml",'r',encoding='utf-8').readlines())) #地图信息

#地图载入
map_data_list = []
size_info = linecache.getline("maps\CE-3",2)

def employee_load(employee,level,reliability,elite_lv,proficiency_lv) #干员名称，等级，信赖度，精英化等级，潜能突破等级
	employee_file_name= employee + ".yml"
	hp_value = linecache.getline(employee_file_name,5)