# coding: UTF-8
# 
import json


def log(level='info',message=''):
	if not isinstance(message,str):
		message = json.dumps(message)
	print('[%s] : %s' % (level,message))