# -*- coding: utf-8 -*-

############################################################
# file : test.py
# 制作 ： tatra 2024年9月5日
# 
# googleカレンダーを使うテスト
#
# 対象バージョン : python 3.x 
# 外部モジュール :
#   google-api-python-client, google-auth-httplib2, google-auth-oauthlib
#	simpleaudio
# メモ :
# 
############################################################

import os
import glob
import subprocess
import re

from tlib import debug_print
from tlib import ffmedia
from tlib.pathutil import *

############################################################
# パスを整える
# メモ:
#   なんかもっといい感じの名前にする
this_file_dir = os.path.dirname(os.path.abspath(__file__))
def path_fix(path):
	return os.path.normpath(os.path.join(this_file_dir,path))


path = path_fix("./close")
print(path)
files = glob.glob(path+"/*")

print(files)

list = [1,2,3,4]

list.append(2)
list.append(5)

print(list)

if __name__ == "__main__":
	res_main = subprocess.Popen(["aplay", "-l"], stdout=subprocess.PIPE )
	res_grep = subprocess.Popen(["grep", "card"], stdin=res_main.stdout, stdout=subprocess.PIPE )
	res_main.stdout.close()
	res = res_grep.communicate()[0]
	res_grep.returncode

	res_str = res.decode("utf-8")
	debug_print.debug_print(res_str)
	res_list = res_str.split('\n')
	debug_print.debug_print(str(res_list))

	for elm in res_list :
		if elm == "" : break
		dev_ret = re.match(r'.*device (?P<device>\d+?):',elm)
		card_ret = re.match(r'^card (?P<card>\d+?):',elm)

		print(card_ret)
		print(dev_ret)
		print(card_ret.group("card"))
		print(dev_ret.group("device"))
		print(card_ret.groupdict())
		print(dev_ret.groupdict())
	"""
	debug_print.debug_print("tesuto")
	fm = ffmedia.ffmedia()
	fm.get_device_list()

	print(__file__)
	abs_file=os.path.abspath(__file__)
	print(abs_file)
	print(this_file_dir)
	join_path = os.path.join(this_file_dir,"./close")
	print(join_path)
	nm_path = os.path.normpath(join_path)
	print(nm_path)

	p = get_dir(__file__,"./close")
	print(p)
	"""