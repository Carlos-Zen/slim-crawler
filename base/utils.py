# coding:utf-8
import re
from base.log import *

'''
巴乐兔，字符串处理，解析数据
'''
REG = {
	'number':r'(\d+)',
	'yuan':r'(\d+)元',
	'huxing':r'(\d)室(\d)厅(\d)卫',
	'floor':r'(\d+)层.*(\d+)层',
	'rent_type':r'(.+?租).*(.+?卧)',
	'payment':r'付(.)押(.)',
	'district_block':r'(.+?)\s+\-\s+(.+)',
	'longi':r'.*var\s+s_lon\s?=\s?\'(-?\d+\.\d+)\';',
	'lati':r'.*var\s+s_lat\s?=\s?\'(-?\d+\.\d+)\';',
}

def splitNumber(string):
	matched = re.search(REG['yuan'],string)
	return matched.group(1)	

def splitYuan(string):
	matched = re.search(REG['number'],string)
	return matched.group(1)

def splitHuxing(string):
	matched = re.match(REG['huxing'],string)
	return matched.group(1),matched.group(2),matched.group(3)

def splitFloor(string):
	matched = re.match(REG['floor'],string)
	return matched.group(1),matched.group(2)

def splitRentType(string):
	matched = re.match(REG['rent_type'],string)
	return matched.group(1),matched.group(2)	

def splitPayment(string):
	matched = re.match(REG['payment'],string)
	return matched.group(1),matched.group(2)

def splitDistrictBlock(string):
	string = string.replace("\n", '')
	matched = re.match(REG['district_block'],string)
	return matched.group(1),matched.group(2)	

def splitLongi(string):
	matched = re.search(REG['longi'],string)
	return matched.group(1)

def splitLati(string):
	matched = re.search(REG['lati'],string)
	return matched.group(1)	

def trim(string):
	'''
	remove \n,space
	'''	
	string = string.replace("\n", '').replace(' ','')
	return string