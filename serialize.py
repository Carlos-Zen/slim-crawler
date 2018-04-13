# coding: UTF-8

import json
import re
from base.serialize import Serialize
from model import House
from base.utils import *
from base.dict import *


class SerializeBlt(Serialize):
	model = House

	def init(self):
		self.data['source'] = 'baletu.com'

	def getattr_basic(self):
		self.data['title'] = self.dom.find('div',{'class':'basic-title'}).find('a').get_text()
		self.data['apartment'] = self.data['title']
		rental = self.dom.find('div',{'class':'house-text-Akey'}).find('li',{'class':'price'}).get_text()
		self.data['rental'] = splitYuan(rental)
		room_area = self.dom.find('div',{'class':'house-text-Akey'}).find('li',{'class':'cent'}).get_text()
		self.data['room_area'] = splitYuan(room_area)
		self.data['orientation'] = self.dom.find('div',{'class':'house-text-Akey'}).find_all('li')[2].get_text()
		self.data['city'] = trim(self.dom.select('div.region a')[0].get_text())

	def getattr_around(self):
		dds = self.dom.find('div',{'class':'house-text-list'}).find_all('dd')
		# print(dds,dds[5].get_text())
		self.data['trafic'] = dds[0].get_text()
		self.data['room_num'],self.data['hall_num'],self.data['bathroom_num'] = splitHuxing(dds[1].get_text())
		self.data['floor'],self.data['building_floor'] = splitFloor(dds[2].get_text())
		rent_type,bedroom_type = splitRentType(dds[3].get_text())
		self.data['floor'],self.data['building_floor'] = v2k('rent_type',rent_type),v2k('bedroom_type',bedroom_type)
		# print(dds[4].get_text())
		payment_rental,payment_deposit = splitPayment(dds[4].get_text())
		self.data['payment_rental'],self.data['payment_deposit'] = chinese_to_arabic(payment_rental),chinese_to_arabic(payment_deposit)
		self.data['district'],self.data['block'] = splitDistrictBlock(dds[5].get_text())
		self.data['address'] = dds[6].get_text()

	def getattr_pictures(self):
		pictures_dom = self.dom.select('div.imagesPreviewer .i-images img')
		self.data['pictures'] = [pdom.get('data-src') for pdom in pictures_dom]

	def getattr_longlat(self):
		html = str(self.dom)
		self.data['longi'] = splitLongi(html)
		self.data['lati'] = splitLati(html) 

	def getattr_falicities(self):
		pri_fal_doms = self.dom.select('div#privateFalicities li img')
		pub_fal_doms = self.dom.select('div#publicFalicities li img')
		self.data['private_falicities'] = [dv2k('baletu','config',fdom.get('alt')) for fdom in pri_fal_doms]
		self.data['public_falicities'] = [dv2k('baletu','config',fdom.get('alt')) for fdom in pub_fal_doms]

class Serialize58(Serialize):
	model = House

	def getattr_nameloc(self):
	    info_1 = re.search(r'(\{\"name.*?\})',self.dom.html.head.script.get_text())
	    info_1_josn = json.loads(info_1.group(0))
	    self.data['name'] = info_1_josn['name']
	    self.data['lati'] = info_1_josn['lat']
	    self.data['longi'] = info_1_josn['lon']

	def getattr_area(self):
	    info_2 = re.search(r'\{\"I\"\:1025.*?\}',self.dom.html.head.script.get_text())
	    info_2_josn = json.loads(info_2.group(0))
	    info_2_area = info_2_josn['V']
	    self.data['room_area'] = info_2_area

	def getattr_price(self):
		"""
		匹配价格
		"""
		info_3 = re.search(r'\{\"I\"\:1016.*?\}',self.dom.html.head.script.get_text())
		info_3_josn = json.loads(info_3.group(0))
		info_3_price = info_3_josn['V']
		self.data['rental'] = info_3_price 

	def getattr_other(self):
		disposals_dom = self.dom.find('ul',{'class':'house-disposal'}).find_all('li')
		self.data['disposals'] = []
		for disposal_dom in disposals_dom:
			self.data['disposals'].append(disposal_dom.get_text())
		

	def getattr_desc(self):
		self.data['title'] = self.dom.find('div',{'class':'house-title'}).find('h1').get_text()
		self.data['address'] = self.dom.find('span',{'class':'dz'}).get_text()
		self.data['rent_type'] = self.dom.find('ul',{'class':'f14'}).find_all('li')[0].find_all('span')[1].get_text()
		self.data['huxing'] = self.dom.find('ul',{'class':'f14'}).find_all('li')[1].find_all('span')[1].get_text()
		self.data['orientation'] = self.dom.find('ul',{'class':'f14'}).find_all('li')[2].find_all('span')[1].get_text()
		self.data['village'] = self.dom.find('ul',{'class':'f14'}).find_all('li')[2].find_all('span')[1].get_text()
		self.data['content'] = self.dom.find('span',{'class':'a2'}).get_text()


class SerializeMogo(Serialize):
	model = House

	def getattr_info(self,bsdom):
		self.data['title'] = bsdom.find('span',{'class':'spacer-m-r10 room-info-tit'}).get_text()

	def getattr_area(self,bsdom):
		self.data['room_area'] = bsdom.find('div',{'class':'room-rs'}).find('ul').get_text()

if __name__ == '__main__':
	h = House()
	s = HouseSerialize('sdf')
	d = s.get()
	print(d)