# coding: UTF-8
import json

class Model:

	def __getitem__(self,key):
		if hasattr(self,key):
			return getattr(self,key)
		else:
			return None

	def __setitem__(self,key,value):
		if hasattr(self,key):
			setattr(self,key,value)
		else:
			pass

	def _create_uniqe_key(self):
		pass

	def __str__(self):
		self._create_uniqe_key()
		return str(self.__dict__.items())

	def json(self):
		self._create_uniqe_key()
		return json.dumps(self.__dict__)
