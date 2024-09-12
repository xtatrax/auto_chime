# -*- coding: utf-8 -*-

############################################################
# file : ffmedia.py
# 制作 ： tatra 2024年9月8日
# 
# ffmpeg Wrapper
#
# 対象バージョン : python 3.x 
# 外部モジュール : yt-dlp
# https://github.com/yt-dlp/yt-dlp/wiki/Installation#with-pip
#
# 外部ソフト :
#	ffmpeg mplayer
# メモ :
#
#	card 0: Headphones [bcm2835 Headphones], device 0: bcm2835 Headphones [bcm2835 Headphones]
#	card 1: vc4hdmi0 [vc4-hdmi-0], device 0: MAI PCM i2s-hifi-0 [MAI PCM i2s-hifi-0]
#	card 2: vc4hdmi1 [vc4-hdmi-1], device 0: MAI PCM i2s-hifi-0 [MAI PCM i2s-hifi-0]
#	↑
#	r'^card ([0-9]+):|, device ([[0-9]+]):'
#
#	ffmpeg -stream_loop -1 -i "path" -f alsa hw:card Num,device Num
############################################################

import os
import sys
import platform
import subprocess


from . import debug_print, pathutil



debug_print.is_debug_print = True
debug_print.debug_print("debug")
"""
	共通
"""
class ffmedia_base():
	# 共通コマンド
	bace_command = ["ffmpeg", "-stream_loop", "-1", "-i"]
	device = ""
	def __init__(self):
		dummy=0

	#
	def play(self, path, exOption=[]):
		command = self.bace_command
		command.append(path)
		command += exOption
		debug_print(" cmmand = " + command)
		# プレイヤーを立ち上げて ffprocess へ パイプ を保存
		self.ffprocess = subprocess.Popen(
			command,
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE
		)

	# 再生停止
	def stop(self):
		# 停止コマンド送信
		self.ffprocess.stdin.write("q")

	# 強制停止
	def kill(self):
		self.ffprocess.kill()

"""
	windows用
"""
class windows(ffmedia_base):
	def __init__(self):
		dummy=0
	#再生
	def play(self, path):
		super().play(path,[
			"-f", "matroska",
			"-map", "0:a",
			"-c", "copy", 
			"-",
			"|",
			"ffplay.exe", "-nodisp",
			"-i", "-"
		])

"""
	linux用
"""
class linux(ffmedia_base):
	def __init__(self):
		dummy=0

	#
	def play(self, path):
		super().play(path)

	"""
		select_sound_device			: 再生デバイスを指定 ex) hw:0,0  ex) hw:card=vc4hdmi0,0  ex)sysdefault:CARD=Headphones 等
		high_priority_sound_device	: select_sound_device が未指定 または 見つからなかったとき 優先的に選択されるデバイス
									: 正規表現  ex) *hdmi*  
									: 上記どちらも見つからない場合とりあえず鳴らせるデバイスを探す。
	"""
	def select_device(self,
					select_sound_device="",
					high_priority_sound_device="",
					select_GPU="",
					high_priority_GPU=""):

		self.device = select_sound_device

		if select_sound_device != "":
			dummy=0
		
	def check_device(self,mdevice):
		test_file_path = pathutil.get_dir(__file__,"test_files","test_wave.wav")


	def get_device_list(self):
		res_main = subprocess.Popen(["aplay", "-l"], stdout=subprocess.PIPE )
		res_grep = subprocess.Popen(["grep", "card"], stdin=res_main.stdout, stdout=subprocess.PIPE )
		res_main.stdout.close()
		res = res_grep.communicate()[0]
		res_grep.returncode

		res_str = res.decode("utf-8")
		debug_print.debug_print(res_str)
		res_list = res_str.split('\n')
		debug_print.debug_print(str(res_list))
		

"""
	ffmpegを個人的に使いやすくするためのあれこれ
"""
class ffmedia():
	#
	def __init__(self):
		self.platform = platform.system()
		#
		if(self.platform == "Windows"):
			self.env_wrap = windows()
		#
		elif(self.platform == "Linux"):
			self.env_wrap = linux()
		#
		#elif(self.platform == "Darwin")
		#
		else:
			#
			raise Exception("未対応のOSです")
	#
	def play(self,path):
		self.env_wrap.play(path)
	#
	def stop(self):
		self.env_wrap.stop()
	#
	def select_device(self,
				select_sound_device="",
				high_priority_sound_device="",
				select_GPU="",
				high_priority_GPU=""):
		self.env_wrap.select_device(
				select_sound_device,
				high_priority_sound_device,
				select_GPU,
				high_priority_GPU)

	def get_device_list(self):
		self.env_wrap.get_device_list()

if __name__ == "__main__":
    debug_print.debug_print("こんにちは")
