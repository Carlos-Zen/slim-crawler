# coding: UTF-8
 
import json
import re

class Serialize:
	dom = None

	def __init__(self,bsdom):
		self.dom = bsdom
		self.data = self.model()

	def init(self):
		pass

	def get(self):
		self.init()
		callfuncs = self.__get_methods()
		for func in callfuncs:
			# try:
			func()
			# except Exception as e:
				# print(e)
		
		return self.data

	def __get_methods(self):
		allattr = dir(self)
		callfuncs = []
		for attr in allattr:
			# print(type(attr),attr)
			if attr.find('getattr_') == 0 and callable(getattr(self,attr)):
				callfuncs.append(getattr(self,attr))
		return callfuncs
