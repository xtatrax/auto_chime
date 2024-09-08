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

from tlib import debug_print
from tlib import ffmedia
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

	fm = ffmedia.ffmedia()
	fm.select_device()
