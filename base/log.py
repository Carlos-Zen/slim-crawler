# coding: UTF-8
# 
import json
import logging
from setting import *

logger = logging.getLogger()

if DEBUG:
	logger.setLevel(logging.DEBUG)
else:	
	logger.setLevel(logging.INFO)
consoleHandler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s") 

consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)