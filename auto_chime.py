# -*- coding: utf-8 -*-

############################################################
# file : auto_chime.py
# 制作 ： tatra 2024年9月5日
# 
# 自動チャイム
#
# 対象バージョン : python 3.x 
# 外部モジュール : pydub
#	https://github.com/jiaaro/pydub
# メモ :
#	[▲]設定ファイル実装
#	[▲]デーモン
#	[]スケジュール
#	[]再生
#	[]再生デバイス指定
#	[]サービス登録
#	[]インストーラー
#	[]ユーザーフレンドリー
#
#	@ UI 実装
#	[] 案 | Apache
#	[] 案 | GUI
#	[] 案 | Google等の外部機能連携
#
#
#
#
#	
############################################################

import os
import json
import time
import argparse
import datetime
import pydub
import glob
#独自ライブラリ
from tlib import xorshift
from tlib import debug_print

############################################################
# 引数定義
parser = argparse.ArgumentParser(description=u'自動チャイムプログラム') #
parser.add_argument('--debug', action='store_true', help=u' --debug デバッグモードで起動') # ありTrue : なしFalse
args = parser.parse_args()



############################################################
# パスを整える
# メモ:
#   なんかもっといい感じの名前にする
this_file_dir = os.path.dirname(__file__)
def path_fix(path):
	return os.path.normpath(os.path.exists(this_file_dir,path))


dbg_var_schedule_json_path = path_fix("/schedule.json")
debug_print(dbg_var_schedule_json_path)


############################################################
# チャイムクラス
class auto_chime:
	#jsondata
	is_play_chime = False
	def __init__(self,json_path):
		f = open(json_path,'r',encoding='utf-8')
		self.jsondata = json.load(f)
		f.close()


	def get_audio_list(self,type):
		dbg_val_tmpDir = this_file_dir
		list = self.jsondata["soundlist"][type]
		audio_list=[]
		for sounds in list:
			temp=sounds
			if os.path.isdir(temp) :
				audio_list.append(path_fix(temp))
			elif False: # URL
				dummy=0
			else:
				dummy=0
			

	def get_play_audio(self):
		tmp=dbg_val_tmpDir + close
		audio_path = os.path.normpath(tmp)
		return audio_path

	def play(self):
		audio_path = self.get_play_audio()

	def chime_job(self):
		is_play_chime=True
		while True:
			time.sleep(1)



def main():
    while True:
        ac = auto_chime(dbg_var_schedule_json_path)
        ac.play()
        time.sleep(60)

if __name__ == "__main__":
    is_debug_print = args.debug
    main()