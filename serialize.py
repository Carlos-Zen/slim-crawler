# coding: UTF-8
import json
import re
from base.serialize import Serialize
from model import House

class SerializeBlt(Serialize):
	model = House

	def getattr_basic(self):
		self.data['title'] = self.dom.find('div',{'class':'basic-title'}).find('a').get_text()
		self.data['apartment'] = self.data['title']
		self.data['rental'] = self.dom.find('div',{'class':'house-text-Akey'}).find('li',{'class':'price'}).get_text()
		self.data['room_area'] = self.dom.find('div',{'class':'house-text-Akey'}).find('li',{'class':'cent'}).get_text()
		self.data['orientation'] = self.dom.find('div',{'class':'house-text-Akey'}).find_all('li')[2].get_text()

	def getattr_around(self):
		dls = self.dom.find('div',{'class':'house-text-list'}).find_all('dl')
		self['']
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