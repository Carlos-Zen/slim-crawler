# coding: UTF-8
 
import json
import re
from base.model import Model

CONFIG = {
	'wardrobe':'wardrobe',
	'sofa':'sofa',
	'tv':'tv',
	'fridge':'fridge',
	'washer':'washer',
	'aircondition':'aircondition',
	'waterheater':'waterheater',
	'broadband':'broadband',
	'heating':'heating',
	'microwave':'microwave',
	'exclusive':'exclusive',
}

class House(Model):
	title = ''
	content = ''
	brand = ''
	province = ''
	city = ''
	district = ''
	block = ''
	address = ''
	lati = ''
	longi =''
	apartment = ''
	rent_type = 0 #整租/合租/公寓
	bedroom_type = 1 #主卧：1，次卧：2
	room_num = 0
	hall_num = 0
	bathroom_num = 0
	floor = 0
	building_floor = 0
	rental = 0
	deposit = 0
	payment_deposit = 1 #付款方式押金月份
	payment_rental = 1 #付款方式租金月份
	orientation = '' #朝向
	deroration = ''
	room_area = 0 #面积
	house_area = 0
	exclusive_bathroom = 0
	exclusive_balcony = 0 
	publish_date = ''
	pictures = []
	source_from = ''
	publisher = ''
	traffic = ''