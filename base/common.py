# coding:utf-8
# 
# 
import hashlib

def md5(str):
	'''
	只适用utf-8编码
	'''
	hl = hashlib.md5()
	hl.update(str.encode(encoding='utf-8'))
	return hl.hexdigest()

